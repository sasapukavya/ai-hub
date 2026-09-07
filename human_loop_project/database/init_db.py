from azure.cosmos import CosmosClient, PartitionKey
import urllib3

urllib3.disable_warnings()

client = CosmosClient(
    "https://cosmos-emulator:8081/",
    credential="C2y--------------------------------------------------------",
    connection_verify=False
)

database = client.create_database_if_not_exists(
    id="EmployeeDB"
)

container = database.create_container_if_not_exists(
    id="Employees",
    partition_key=PartitionKey(path="/department")
)

employees = [
    {
        "id": "1",
        "name": "John",
        "department": "IT",
        "salary": 80000
    },
    {
        "id": "2",
        "name": "Emma",
        "department": "HR",
        "salary": 60000
    },
    {
        "id": "3",
        "name": "David",
        "department": "Finance",
        "salary": 90000
    },
    {
        "id": "4",
        "name": "Sophia",
        "department": "IT",
        "salary": 75000
    },
    {
        "id": "5",
        "name": "Michael",
        "department": "Sales",
        "salary": 55000
    },
    {
        "id": "6",
        "name": "Olivia",
        "department": "Marketing",
        "salary": 68000
    },
    {
        "id": "7",
        "name": "James",
        "department": "Support",
        "salary": 50000
    },
    {
        "id": "8",
        "name": "Ava",
        "department": "Operations",
        "salary": 72000
    },
    {
        "id": "9",
        "name": "William",
        "department": "Admin",
        "salary": 65000
    },
    {
        "id": "10",
        "name": "Isabella",
        "department": "IT",
        "salary": 85000
    }
]

for emp in employees:
    container.upsert_item(emp)

print("EmployeeDB created successfully.")
print("Employees inserted successfully.")
