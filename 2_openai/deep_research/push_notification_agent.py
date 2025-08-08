import os
from typing import Dict
import requests
from agents import Agent, function_tool

@function_tool
def send_notification(subject: str, message: str) -> Dict[str, str]:
    """ Send a push notification with the given subject and message """
    pushover_user = os.environ.get('PUSHOVER_USER')
    pushover_token = os.environ.get('PUSHOVER_TOKEN')
    
    if not pushover_user or not pushover_token:
        raise RuntimeError("Missing PUSHOVER_USER or PUSHOVER_TOKEN in environment")

    payload = {
        "user": pushover_user, 
        "token": pushover_token, 
        "title": subject,
        "message": message
    }
    
    response = requests.post("https://api.pushover.net/1/messages.json", data=payload)
    print("Notification response", response.status_code)
    response.raise_for_status()
    return {"status": "success"}

INSTRUCTIONS = """You are able to send a concise push notification based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one notification with 
an appropriate title and a summary of the key findings (keep the message under 1024 characters)."""

notification_agent = Agent(
    name="Notification agent",
    instructions=INSTRUCTIONS,
    tools=[send_notification],
    model="gpt-4o-mini",
)
