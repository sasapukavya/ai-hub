import os
import uuid
import urllib3

from datetime import datetime
from azure.cosmos import CosmosClient

urllib3.disable_warnings()

# ==========================================================
# Cosmos Connection
# ==========================================================

COSMOS_URL = os.getenv(
    "COSMOS_ENDPOINT",
    "https://cosmos-emulator:8081/"
)

COSMOS_KEY = os.getenv(
    "COSMOS_KEY",
    "C2y---------------------------------------------------------------------"
)

client = CosmosClient(
    COSMOS_URL,
    credential=COSMOS_KEY,
    connection_verify=False
)

database = client.get_database_client("EmployeeDB")

container = database.get_container_client("Feedback")


# ==========================================================
# Save Feedback
# ==========================================================

def save_feedback(question, plan, approved):

    item = {
        "id": str(uuid.uuid4()),
        "question": question,
        "agent": plan["agent"],
        "tool": plan.get("tool"),
        "tool_input": plan.get("tool_input"),
        "approved": approved,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    container.create_item(item)

    return item


# ==========================================================
# Get All Feedback
# ==========================================================

def get_feedback():

    feedback = list(

        container.query_items(

            query="SELECT * FROM c",

            enable_cross_partition_query=True

        )

    )

    return feedback
