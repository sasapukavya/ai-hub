from database.cosmos_db import (
    get_employees,
    get_employee_count,
    get_employee_by_name,
    get_employees_by_department,
    get_highest_salary_employee,
    get_average_salary,
    get_salary_above,
    get_departments,
    add_employee
)


class DatabaseTool:

    def query(self, sql_query):

        print("\n================ DATABASE TOOL ================")
        print(sql_query)
        print("===============================================")

        query = sql_query.lower().strip()

        try:

            # -------------------------------------------------
            # INSERT EMPLOYEE
            # -------------------------------------------------
            if query.startswith("insert"):

                values = sql_query.split("VALUES")[1]

                values = (
                    values.replace("(", "")
                    .replace(")", "")
                    .replace(";", "")
                )

                values = [
                    value.strip().replace("'", "")
                    for value in values.split(",")
                ]

                employee_id = values[0]
                name = values[1]
                department = values[2]
                salary = int(values[3])

                return add_employee(
                    employee_id,
                    name,
                    department,
                    salary
                )

            # -------------------------------------------------
            # COUNT
            # -------------------------------------------------
            elif "count" in query:

                return get_employee_count()

            # -------------------------------------------------
            # AVERAGE SALARY
            # -------------------------------------------------
            elif "avg" in query:

                return get_average_salary()

            # -------------------------------------------------
            # HIGHEST SALARY
            # -------------------------------------------------
            elif "order by" in query and "salary" in query:

                return get_highest_salary_employee()

            # -------------------------------------------------
            # SALARY >
            # -------------------------------------------------
            elif "salary >" in query:

                amount = int(
                    query.split(">")[1]
                    .replace(";", "")
                    .strip()
                )

                return get_salary_above(amount)

            # -------------------------------------------------
            # DEPARTMENT
            # -------------------------------------------------
            elif "department" in query:

                departments = get_departments()

                for dept in departments:

                    if dept.lower() in query:

                        return get_employees_by_department(dept)

                return []

            # -------------------------------------------------
            # EMPLOYEE NAME
            # -------------------------------------------------
            else:

                employees = get_employees()

                for employee in employees:

                    if employee["name"].lower() in query:

                        return get_employee_by_name(
                            employee["name"]
                        )

                return employees

        except Exception as e:

            print("\n============= DATABASE ERROR =============")
            print(e)
            print("==========================================")

            return {
                "success": False,
                "message": str(e)
            }