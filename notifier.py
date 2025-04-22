import os
import smtplib
import requests
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_slack(message: str):
    webhook = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook:
        raise ValueError("SLACK_WEBHOOK_URL not set")
    requests.post(webhook, json={"text": message})

def alert(event_name: str, message: str):
     send_slack(message)

