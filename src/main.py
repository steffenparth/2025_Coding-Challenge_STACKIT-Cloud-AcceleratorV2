from fastapi import FastAPI

from src.schema.notification_schema import DefaultNotification
from src.storage.notifications_in_memory import saved_notifications
from src.bot.telegram_bot import forwarding_warning_message

import asyncio

app = FastAPI()


@app.post("/notifications")
def receive_notifications(notification: DefaultNotification):

    saved_notifications.append(notification)

    if notification.Type == "Warning":
        print("Warning received")
        asyncio.run(forwarding_warning_message(str(notification)))
        return {"message": "Warning received"}
    print("message received")
    return {"message": "Notification received"}