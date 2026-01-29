import json

files = ["semgrep.json", "trivy.json", "gitleaks.json"]
combined = {}

for f in files:
    try:
        with open(f) as file:
            combined[f] = json.load(file)
    except Exception as e:
        combined[f] = {"error": str(e)}

with open("combined.json", "w") as out:
    json.dump(combined, out, indent=2)

print("Combined report generated → combined.json")
