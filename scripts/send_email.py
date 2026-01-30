import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timezone, timedelta
import os

sender = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASS")
receiver = os.getenv("RECEIVER_EMAIL")

if not sender or not password or not receiver:
    raise ValueError(
        f"Missing env vars → sender={sender}, password={'set' if password else None}, receiver={receiver}"
    )

# IST timezone - UTC + 5:30
IST = timezone(timedelta(hours=5, minutes=30))
timestamp = datetime.now(IST).strftime("%Y-%m-%d %H:%M IST")

with open("ai-summary.txt") as f:
    body = f.read()

msg = MIMEText(body)
msg["Subject"] = "🚨 AI Security Scan Summary - CI Pipeline | {timestamp}"
msg["From"] = sender
msg["To"] = receiver

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.send_message(msg)

print("Security summary email sent successfully")
