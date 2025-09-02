from telegram import Bot
from ..dependencies import credentials
import os

async def forwarding_warning_message(message: str):
    """
    if telegram credentials are set, a message is forwarded to telegram bot
    """

    if not credentials.TELEGRAM_BOT_TOKEN or not credentials.TELEGRAM_CHAT_ID:
        print("No telegram token or chat id found")
        raise Exception("No telegram token or chat id found")

    try:
        bot = Bot(token=credentials.TELEGRAM_BOT_TOKEN)
        await bot.send_message(chat_id=credentials.TELEGRAM_CHAT_ID, text=message)
        print("Warning message sent to telegram")
    except Exception as e:
        print(f"Error forwarding warning message to telegram: {e}")
