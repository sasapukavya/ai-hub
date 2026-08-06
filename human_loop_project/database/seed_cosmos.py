from azure.cosmos import CosmosClient, PartitionKey
import urllib3

urllib3.disable_warnings()

URL = "https://cosmos-emulator:8081/"

KEY = "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=="

DATABASE_NAME = "EmployeeDB"
CONTAINER_NAME = "Employees"

client = CosmosClient(
    URL,
    credential=KEY,
    connection_verify=False
)

# Create database if it doesn't exist
database = client.create_database_if_not_exists(
    id=DATABASE_NAME
)

# Create container if it doesn't exist
container = database.create_container_if_not_exists(
    id=CONTAINER_NAME,
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

# Insert employees into Cosmos DB
for employee in employees:
    container.upsert_item(employee)

print(f"{len(employees)} employees inserted into Cosmos DB successfully!")