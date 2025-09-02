from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_CHAT_ID: str
    NOTIFICATIONS_PW: str
    model_config = SettingsConfigDict(env_file="../.env")

credentials = Settings()
