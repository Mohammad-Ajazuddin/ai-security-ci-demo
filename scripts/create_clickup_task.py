import requests
import os
from datetime import datetime

CLICKUP_TOKEN = os.getenv("CLICKUP_TOKEN")
LIST_ID = os.getenv("CLICKUP_LIST_ID")

if not CLICKUP_TOKEN or not LIST_ID:
    raise ValueError("Missing CLICKUP_TOKEN or CLICKUP_LIST_ID")

with open("ai-summary.txt") as f:
    content = f.read()

# Generate timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

task_name = f"🚨 Security Issues - {timestamp}"

url = f"https://api.clickup.com/api/v2/list/{LIST_ID}/task"

headers = {
    "Authorization": CLICKUP_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "name": task_name,
    "description": content,
    "priority": 1
}

response = requests.post(url, json=payload, headers=headers)

print("ClickUp Status Code:", response.status_code)
print("ClickUp Task Name:", task_name)
