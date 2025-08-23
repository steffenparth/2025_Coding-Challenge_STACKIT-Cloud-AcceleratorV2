from pydantic import BaseModel

class DefaultNotification(BaseModel):
    Type: str
    Name: str
    Description: str