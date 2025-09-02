from pydantic import BaseModel, Field, Strict
from enum import Enum

class DefaultNotificationTypes(str, Enum):
    Info = "Info"
    Warning = "Warning"
    Error = "Error"


class DefaultNotification(BaseModel):
    """
    Represents a default notification with a specified type, name, and description.

    This class is a model for default notifications, used to structure and validate
    the attributes of a notification. It ensures that the `Name` and `Description`
    attributes meet specified criteria regarding length.

    Attributes:
    Type:
        The type of the notification, represented by DefaultNotificationTypes.
    Name:
        The name of the notification with a minimum length of 1 and a maximum of 100.
    Description:
        A description of the notification with a minimum length of 1 and a maximum of 500.
    """

    Type: DefaultNotificationTypes
    Name: str = Field(..., min_length=1, max_length=100)
    Description: str = Field(..., min_length=1, max_length=500)

    # """
    # Type, Name and Description must be specified,
    # additional values are ignored
    # """