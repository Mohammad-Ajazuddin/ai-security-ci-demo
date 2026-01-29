from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("combined.json") as f:
    data = f.read()

prompt = f"""
You are a senior application security engineer.

Analyze the following security scan report.

MANDATORY:
1. List **ALL detected secrets individually** (cloud keys, API keys, DB passwords, tokens, etc).
2. Categorize issues into: CRITICAL, HIGH, MEDIUM, LOW.
3. Provide an executive summary.
4. Suggest remediation steps.

Report:
{data}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2,
)

analysis = response.choices[0].message.content

with open("ai-summary.txt", "w") as f:
    f.write(analysis)

print("AI security analysis generated → ai-summary.txt")
