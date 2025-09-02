from fastapi import FastAPI
from .routers import notification_router


app = FastAPI()

app.include_router(notification_router.router)