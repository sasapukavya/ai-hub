from azure.cosmos import CosmosClient, PartitionKey
import urllib3

urllib3.disable_warnings()

COSMOS_URL = "https://cosmos-emulator:8081/"

COSMOS_KEY = "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=="

client = CosmosClient(
    COSMOS_URL,
    credential=COSMOS_KEY,
    connection_verify=False
)

print("Connected to Cosmos Emulator")

database = client.create_database_if_not_exists(
    id="EmployeeDB"
)

print("Database created")

container = database.create_container_if_not_exists(
    id="Employees",
    partition_key=PartitionKey(path="/department")
)

print("Container created")