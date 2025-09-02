from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..schema.notification_schema import DefaultNotification
from ..storage.notifications_in_memory import saved_notifications
from ..bot.telegram_bot import forwarding_warning_message
from ..dependencies import credentials

router = APIRouter()

@router.post("/notifications")
async def receive_notifications(notification: DefaultNotification):
    """
    notifications getting stored -
    notifications of "Type": "Warning" are forwarded to telegram bot"

    - **Type (required)**: Notification type (must be one of: `"Info"`, `"Warning"`, `"Error"`)
    - **Name (required)**: Short title of the notification (1–100 characters)
    - **Description (required)**: Detailed description of the notification (1–500 characters)
    - **Additional parameters**: Additional parameters can be added to the notification, but are ignored.
    """

    saved_notifications.append(notification)

    if notification.Type == "Warning":
        chat_message = f"Warning: {notification.Name}\n\n{notification.Description}"

        try:
            await forwarding_warning_message(chat_message)
            print("Warning received and forwarded to telegram")
            return {"message": "Warning received, saved and forwarded to telegram"}
        except Exception as e:
            print(f"Error forwarding warning to telegram: {e}")
            return JSONResponse(
                status_code=202,
                content={"message": "Warning received and saved. Forward to Telegram failed!"},
            )

    print("message received")
    return {"message": "Notification received and saved"}

@router.post("/entries")
async def list_notifications(pw: str):
    """
    list saved notifications if password is correct
    """

    if not credentials.NOTIFICATIONS_PW:
        print("Password not set")
        return JSONResponse(
            status_code=500,
            content={"message": "Server Error: Password not set"},
        )

    if pw != credentials.NOTIFICATIONS_PW:
        print("Password not correct")
        return JSONResponse(
            status_code=401,
            content={"message": "Unauthorized"},
        )
    print("Password valid, listing notifications")
    return saved_notifications