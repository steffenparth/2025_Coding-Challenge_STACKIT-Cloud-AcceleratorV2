from pydantic import BaseModel, Field, Strict
from enum import Enum

class DefaultNotificationTypes(str, Enum):
    Info = "Info"
    Warning = "Warning"
    Error = "Error"


class DefaultNotification(BaseModel):
    """
    Type, Name and Description must be specified,
    additional values are ignored

    - **Type (required)**: Notification type (must be one of: `"Info"`, `"Warning"`, `"Error"`)
    - **Name (required)**: Short title of the notification (1–100 characters)
    - **Description (required)**: Detailed description of the notification (1–500 characters)
    """

    Type: DefaultNotificationTypes
    Name: str = Field(..., min_length=1, max_length=100)
    Description: str = Field(..., min_length=1, max_length=500)
