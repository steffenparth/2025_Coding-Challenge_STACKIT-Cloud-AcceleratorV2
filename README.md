# 2025_Coding-Challenge_STACKIT-Cloud-Accelerator

### run the app
uv run fastapi dev src/main.py

### run the tests
uv run pytest

#### <your_bot_token> ?

1. Open Telegram, search for @BotFather and start a conversation
2. create a new bot with the /newbot command
3. Give the bot a name and a username
4. You will receive the token

#### <your_chat_id> ?
1. Open Telegram, search for your bot and start a conversation
2. Open: https://api.telegram.org/bot<your_bot_token>/getUpdates
3. You shoud see a id field. This is your <your_chat_id>. (If you don't see it send another message to your bot / refresh the page)


export TELEGRAM_BOT_TOKEN=<your_bot_token>
export TELEGRAM_CHAT_ID=<your_chat_id>