from fastapi import FastAPI

from src.schema.notification_schema import DefaultNotification
from src.storage.notifications_in_memory import saved_notifications

app = FastAPI()


@app.post("/notifications")
def read_root(notification: DefaultNotification):

    saved_notifications.append(notification)

    if notification.Type == "Warning":
        print("Warning received")
        return {"message": "Warning received"}
    print("message received")
    return {"message": "message received"}