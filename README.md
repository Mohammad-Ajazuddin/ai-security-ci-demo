# ai-security-ci-demo 🚨🤖

An AI-powered DevSecOps CI pipeline that automatically detects security issues, analyzes them using AI, and creates actionable alerts.

This project demonstrates how modern teams can **shift security left** by combining open-source security tools, CI automation, and AI-driven analysis.

---

## ✨ What This Project Does

On every code push to the `main` branch, the pipeline automatically:

- Scans source code for security issues and bad practices  
- Detects vulnerable third-party dependencies  
- Detects leaked secrets (API keys, passwords, tokens)  
- Combines all findings into a single security report  
- Uses AI to:
  - Classify issues by severity  
  - Generate a human-readable security summary  
  - Suggest remediation steps  
- Sends an email alert with the AI summary  
- Creates a timestamped ClickUp task for tracking and accountability  

---

## 🔁 High-Level Flow

Developer → Push Code
→ GitHub Actions CI
→ Security Scans (Semgrep, Trivy, Gitleaks)
→ Combined Security Report
→ AI Analysis
→ 📧 Email Alert
→ 📌 ClickUp Task


---

## 🛠 Tools & Technologies Used

- **GitHub Actions** – CI orchestration  
- **Semgrep** – Static code security analysis (SAST)  
- **Trivy** – Dependency & filesystem vulnerability scanning  
- **Gitleaks** – Secret detection (API keys, passwords, tokens)  
- **OpenAI API** – AI-based risk analysis and summarization  
- **ClickUp API** – Automatic task creation  
- **Python & Node.js** – Glue logic and demo application  

All security tools used are **free and open source**.

---

## 🎯 Why This Matters

- Prevents accidental exposure of secrets  
- Detects vulnerabilities early in the development lifecycle  
- Converts raw scan data into **actionable insights**  
- Reduces manual security review effort  
- Improves auditability and accountability  

This project is inspired by **real-world DevSecOps practices** used in enterprise environments.

---

## 📌 Demo Highlights

- Fully automated (no manual steps)  
- AI-generated executive security summary  
- Timestamped alerts (IST timezone)  
- Task tracking to ensure issues are not ignored  

---

## ⚠️ Note

This repository is for **demo and learning purposes**.  
Secrets included in the code are intentionally insecure to demonstrate detection.

---

## 📣 Use Cases

- DevSecOps demos  
- CI/CD security automation reference  
- Portfolio / interview showcase  
- Learning modern security pipelines  

