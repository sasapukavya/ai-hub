from database.cosmos_db import (
    get_employees,
    get_employees_by_department,
    get_employee_count,
    get_employee_by_name,
    get_highest_salary_employee,
    get_average_salary,
    get_salary_above,
    get_departments,
    add_employee,
    update_employee_salary,
    delete_employee
)


def employee_tool(action, value=None):

    if action == "all":
        return get_employees()

    elif action == "count":
        return get_employee_count()

    elif action == "department":
        return get_employees_by_department(value)

    elif action == "name":
        return get_employee_by_name(value)

    elif action == "highest_salary":
        return get_highest_salary_employee()

    elif action == "average_salary":
        return get_average_salary()

    elif action == "salary_above":
        return get_salary_above(int(value))

    elif action == "departments":
        return get_departments()

    elif action == "delete":
        return delete_employee(value)

    else:
        return {
            "error": "Invalid action"
        }