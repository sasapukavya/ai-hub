from cosmos.cosmos_client import container


class CosmosTool:

    def get_all_employees(self):

        items = list(container.read_all_items())

        return items

    def employees_by_department(self, department):

        query = """
        SELECT * FROM c
        WHERE c.department=@department
        """

        parameters = [
            {
                "name": "@department",
                "value": department
            }
        ]

        items = list(

            container.query_items(

                query=query,
                parameters=parameters,
                enable_cross_partition_query=True

            )

        )

        return items

    def employees_salary_gt(self, salary):

        query = """
        SELECT * FROM c
        WHERE c.salary>@salary
        """

        parameters = [
            {
                "name": "@salary",
                "value": salary
            }
        ]

        items = list(

            container.query_items(

                query=query,
                parameters=parameters,
                enable_cross_partition_query=True

            )

        )

        return items

    def employee_by_name(self, name):

        query = """
        SELECT * FROM c
        WHERE LOWER(c.name)=LOWER(@name)
        """

        parameters = [
            {
                "name": "@name",
                "value": name
            }
        ]

        items = list(

            container.query_items(

                query=query,
                parameters=parameters,
                enable_cross_partition_query=True

            )

        )

        return items