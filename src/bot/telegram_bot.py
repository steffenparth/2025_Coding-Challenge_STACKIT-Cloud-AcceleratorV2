from telegram import Bot
from ..dependencies import credentials
import os

async def forwarding_warning_message(message: str):
    """
    if telegram credentials are set, a message is forwarded to telegram bot
    """

    try:
        bot = Bot(token=credentials.TELEGRAM_BOT_TOKEN)
        await bot.send_message(chat_id=credentials.TELEGRAM_CHAT_ID, text=message)
        print("Warning message sent to telegram")
    except Exception as e:
        print(f"Error forwarding warning message to telegram: {e}")
        raise
