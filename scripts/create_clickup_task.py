import requests
import os

CLICKUP_TOKEN = os.getenv("CLICKUP_TOKEN")
LIST_ID = os.getenv("CLICKUP_LIST_ID")

with open("ai-summary.txt") as f:
    content = f.read()

#url = f"https://api.clickup.com/api/v2/list/{LIST_ID}/task"

url = f"https://app.clickup.com/37403503/v/l/li/{LIST_ID}/task"

headers = {
    "Authorization": CLICKUP_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "name": "🚨 Security Issues Detected - CI Pipeline",
    "description": content,
    "priority": 1
}

response = requests.post(url, json=payload, headers=headers)

print("ClickUp Task Status:", response.status_code)
