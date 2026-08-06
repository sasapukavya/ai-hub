import json
import os
from datetime import datetime


LOG_FILE = "logs/actions.json"


def log_action(question,
               agent,
               tool,
               approved,
               response):

    os.makedirs("logs", exist_ok=True)

    if os.path.exists(LOG_FILE):

        with open(LOG_FILE, "r") as f:
            logs = json.load(f)

    else:

        logs = []

    logs.append(

        {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "question": question,
            "agent": agent,
            "tool": tool,
            "approved": approved,
            "response": response
        }

    )

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)