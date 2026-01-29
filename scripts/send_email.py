import smtplib
from email.mime.text import MIMEText
import os

sender = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASS")
receiver = os.getenv("RECEIVER_EMAIL")

with open("ai-summary.txt") as f:
    body = f.read()

msg = MIMEText(body)
msg["Subject"] = "🚨 AI Security Scan Summary - CI Pipeline"
msg["From"] = sender
msg["To"] = receiver

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.send_message(msg)

print("Security summary email sent successfully")
