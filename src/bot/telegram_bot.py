from telegram import Bot
import os

async def forwarding_warning_message(message: str):
    """
    if telegram credentials are set, a message is forwarded to telegram bot
    """

    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not telegram_token or not telegram_chat_id:
        print("No telegram token or chat id found")
        raise Exception("No telegram token or chat id found")

    try:
        bot = Bot(token=telegram_token)
        await bot.send_message(chat_id=telegram_chat_id, text=message)
        print("Warning message sent to telegram")
    except Exception as e:
        print(f"Error forwarding warning message to telegram: {e}")
