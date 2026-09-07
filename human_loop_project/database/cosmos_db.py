import os
import urllib3
from azure.cosmos import CosmosClient

urllib3.disable_warnings()

COSMOS_URL = os.getenv(
    "COSMOS_ENDPOINT",
    "https://cosmos-emulator:8081/"
)

COSMOS_KEY = os.getenv(
    "COSMOS_KEY",
    "C2y----------------------------------------------------------------"
)

client = CosmosClient(
    COSMOS_URL,
    credential=COSMOS_KEY,
    connection_verify=False
)

database = client.get_database_client("EmployeeDB")
container = database.get_container_client("Employees")


# ---------------------------------
# Get All Employees
# ---------------------------------
def get_employees():

    return list(
        container.query_items(
            query="SELECT * FROM c",
            enable_cross_partition_query=True
        )
    )


# ---------------------------------
# Get Employees By Department
# ---------------------------------
def get_employees_by_department(department):

    return list(
        container.query_items(
            query="SELECT * FROM c WHERE c.department=@dept",
            parameters=[
                {
                    "name": "@dept",
                    "value": department
                }
            ],
            enable_cross_partition_query=True
        )
    )


# ---------------------------------
# Get Employee By Name
# ---------------------------------
def get_employee_by_name(name):

    return list(
        container.query_items(
            query="SELECT * FROM c WHERE c.name=@name",
            parameters=[
                {
                    "name": "@name",
                    "value": name
                }
            ],
            enable_cross_partition_query=True
        )
    )


# ---------------------------------
# Highest Salary Employee
# ---------------------------------
def get_highest_salary_employee():

    return list(
        container.query_items(
            query="SELECT TOP 1 * FROM c ORDER BY c.salary DESC",
            enable_cross_partition_query=True
        )
    )


# ---------------------------------
# Employee Count
# ---------------------------------
def get_employee_count():

    result = list(
        container.query_items(
            query="SELECT VALUE COUNT(1) FROM c",
            enable_cross_partition_query=True
        )
    )

    return result[0]


# ---------------------------------
# Average Salary
# ---------------------------------
def get_average_salary():

    employees = get_employees()

    if len(employees) == 0:
        return 0

    total = sum(
        emp["salary"]
        for emp in employees
    )

    return total / len(employees)


# ---------------------------------
# Salary Above
# ---------------------------------
def get_salary_above(amount):

    return list(
        container.query_items(
            query="SELECT * FROM c WHERE c.salary>@salary",
            parameters=[
                {
                    "name": "@salary",
                    "value": amount
                }
            ],
            enable_cross_partition_query=True
        )
    )


# ---------------------------------
# Departments
# ---------------------------------
def get_departments():

    employees = get_employees()

    return sorted(
        list(
            set(
                emp["department"]
                for emp in employees
            )
        )
    )


# ---------------------------------
# Add Employee
# ---------------------------------
def add_employee(employee_id, name, department, salary):

    employee = {
        "id": str(employee_id),
        "name": name,
        "department": department,
        "salary": int(salary)
    }

    container.upsert_item(employee)

    return {
        "success": True,
        "message": f"Employee '{name}' added successfully."
    }


# ---------------------------------
# Update Employee Salary
# ---------------------------------
def update_employee_salary(name, salary):

    employees = list(
        container.query_items(
            query="SELECT * FROM c WHERE c.name=@name",
            parameters=[
                {
                    "name": "@name",
                    "value": name
                }
            ],
            enable_cross_partition_query=True
        )
    )

    if len(employees) == 0:
        return {
            "success": False,
            "message": f"Employee '{name}' not found."
        }

    employee = employees[0]

    employee["salary"] = int(salary)

    container.replace_item(
        item=employee["id"],
        body=employee
    )

    return {
        "success": True,
        "message": f"{name}'s salary updated to {salary}."
    }
# ---------------------------------
# Delete Employee
# ---------------------------------
def delete_employee(name):

    try:
        employees = get_employee_by_name(name)

        if len(employees) == 0:
            return {
                "success": False,
                "message": f"Employee '{name}' not found."
            }

        employee = employees[0]

        container.delete_item(
            item=employee["id"],
            partition_key=employee["department"]
        )

        return {
            "success": True,
            "message": f"Employee '{name}' deleted successfully."
        }

    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }
