from fastapi import FastAPI
import os

from src.schema.notification_schema import DefaultNotification
from src.storage.notifications_in_memory import saved_notifications
from src.bot.telegram_bot import forwarding_warning_message

import asyncio

app = FastAPI()


@app.post("/notifications")
def receive_notifications(notification: DefaultNotification):
    """
    notifications getting stored in saved_notifications
    notifications of "Type": "Warning" are forwarded to telegram bot"
    """

    saved_notifications.append(notification)

    if notification.Type == "Warning":
        print("Warning received")
        asyncio.run(forwarding_warning_message(str(notification)))
        return {"message": "Warning received"}
    print("message received")
    return {"message": "Notification received"}

@app.post("/entries")
def list_notifications(pw: str):
    """
    list saved notifications if password is correct
    """

    password = os.getenv("NOTIFICATIONS_PW")
    if not password:
        print("Password not set")
        return {"message": "Password not set"}
    if pw != password:
        print("Password not correct")
        return {"message": "Invalid password"}

    print("Password valid, listing notifications")
    return saved_notifications