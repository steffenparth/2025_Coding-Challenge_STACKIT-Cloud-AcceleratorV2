from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

from src.schema.notification_schema import DefaultNotification
from src.storage.notifications_in_memory import saved_notifications
from src.bot.telegram_bot import forwarding_warning_message


app = FastAPI()


@app.post("/notifications")
async def receive_notifications(notification: DefaultNotification):
    """
    notifications getting stored in saved_notifications
    notifications of "Type": "Warning" are forwarded to telegram bot"
    """

    saved_notifications.append(notification)

    if notification.Type == "Warning":
        chat_message = f"Warning: {notification.Name}\n\n{notification.Description}"

        try:
            await forwarding_warning_message(chat_message)
            print("Warning received and forwarded to telegram")
            return {"message": "Warning received and forwarded to telegram"}
        except Exception as e:
            print(f"Error forwarding warning to telegram: {e}")
            return JSONResponse(
                status_code=202,
                content={"message": "Warning received, forward to Telegram failed"},
            )

    print("message received")
    return {"message": "Notification received"}

@app.post("/entries")
async def list_notifications(pw: str):
    """
    list saved notifications if password is correct
    """

    password = os.getenv("NOTIFICATIONS_PW")
    if not password:
        print("Password not set")
        return JSONResponse(
            status_code=500,
            content={"message": "Server Error: Password not set"},
        )

    if pw != password:
        print("Password not correct")
        return JSONResponse(
            status_code=401,
            content={"message": "Unauthorized"},
        )
    print("Password valid, listing notifications")
    return saved_notifications