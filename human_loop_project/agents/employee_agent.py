from tools.employee_tool import employee_tool


class EmployeeAgent:

    def run(self, question):

        q = question.lower()

        if "all" in q:
            return employee_tool("all")

        elif "it" in q:
            return employee_tool("department", "IT")

        elif "hr" in q:
            return employee_tool("department", "HR")

        elif "finance" in q:
            return employee_tool("department", "Finance")

        elif "john" in q:
            return employee_tool("name", "John")

        elif "emma" in q:
            return employee_tool("name", "Emma")

        elif "david" in q:
            return employee_tool("name", "David")

        elif "sophia" in q:
            return employee_tool("name", "Sophia")

        else:
            return employee_tool("all")