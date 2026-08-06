from azure.cosmos import CosmosClient, PartitionKey
import os
import urllib3

urllib3.disable_warnings()

COSMOS_URL = os.getenv(
    "COSMOS_ENDPOINT",
    "https://cosmos-emulator:8081/"
)

COSMOS_KEY = os.getenv(
    "COSMOS_KEY",
    "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=="
)

client = CosmosClient(
    COSMOS_URL,
    credential=COSMOS_KEY,
    connection_verify=False
)

database = client.create_database_if_not_exists(
    id="EmployeeDB"
)

database.create_container_if_not_exists(
    id="Feedback",
    partition_key=PartitionKey(path="/approved")
)

print("✅ Feedback container created successfully.")