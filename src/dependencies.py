from pydantic_settings import BaseSettings, SettingsConfigDict
import sys

class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_CHAT_ID: str
    NOTIFICATIONS_PW: str
    model_config = SettingsConfigDict(env_file=".env")

try:
    credentials = Settings()
except Exception as e:
    print(f"Failed to load required credentials from .env : {e}")
    sys.exit(1)
