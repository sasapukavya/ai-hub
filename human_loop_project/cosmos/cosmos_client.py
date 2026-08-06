import os
import urllib3
from azure.cosmos import CosmosClient

# Disable SSL warnings for Cosmos Emulator
urllib3.disable_warnings()

COSMOS_URL = os.getenv(
    "COSMOS_ENDPOINT",
    "https://cosmos-emulator:8081/"
)

COSMOS_KEY = os.getenv(
    "COSMOS_KEY",
    "C2y6yD---------------------------------------"
)

DATABASE_NAME = "EmployeeDB"
CONTAINER_NAME = "Employees"

client = CosmosClient(
    COSMOS_URL,
    credential=COSMOS_KEY,
    connection_verify=False
)

database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)