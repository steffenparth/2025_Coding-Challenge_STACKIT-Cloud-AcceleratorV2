from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


saved_notifications = []

class DefaultNotification(BaseModel):
    Type: str
    Name: str
    Description: str


@app.post("/notifications")
def read_root(notification: DefaultNotification):

    saved_notifications.append(notification)

    if notification.Type == "Warning":
        print("Warning received")
        return {"message": "Warning received"}
    print("message received")
    return {"message": "message received"}