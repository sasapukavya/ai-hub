import sqlite3
import os


DB_PATH = "database/employees.db"


def create_database():

    os.makedirs(
        "database",
        exist_ok=True
    )


    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS employees
        (
            id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            salary INTEGER
        )
        """
    )


    employees = [

        (1, "John", "IT", 80000),

        (2, "Emma", "HR", 60000),

        (3, "David", "Finance", 90000),

        (4, "Sophia", "IT", 75000)

    ]


    cursor.executemany(
        """
        INSERT OR IGNORE INTO employees
        VALUES (?, ?, ?, ?)
        """,
        employees
    )


    connection.commit()

    connection.close()


    print("Database created successfully")


if __name__ == "__main__":

    create_database()