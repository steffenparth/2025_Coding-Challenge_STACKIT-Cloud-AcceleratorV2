from pydantic import BaseModel

class DefaultNotification(BaseModel):
    """
    Type, Name and Description must be specified,
    additional values are ignored
    """

    Type: str
    Name: str
    Description: str