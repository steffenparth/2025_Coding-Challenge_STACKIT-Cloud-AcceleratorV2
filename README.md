# 2025_Coding-Challenge_STACKIT-Cloud-Accelerator

A FastAPI-based notification system that saves notifications in memory and forwards warning notifications to a Telegram messenger.

## Features

- RESTful API for managing notifications
- In-memory storage for notifications
- Telegram bot integration for forwarding warning notifications
- Automated testing with pytest
- Built with FastAPI

## Prerequisites

- Python 3.13 or higher
- pipx

## Setup

### 1. Install uv

```bash
pipx install uv
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Credentials for Telegram Bot and Notification Password

#### <your_bot_token> 

1. Open Telegram, search for @BotFather and start a conversation
2. create a new bot with the /newbot command
3. Give the bot a name and a username
4. You will receive the token

#### <your_chat_id> 
1. Open Telegram, search for your bot and start a conversation
2. Open: https://api.telegram.org/bot<your_bot_token>/getUpdates
3. You shoud see a id field. This is your <your_chat_id>. (If you don't see it send another message to your bot / refresh the page)

#### <your_notification_password>
Choose a password of your choice

4. Export the credentials as environment variables:

```bash
export TELEGRAM_BOT_TOKEN=<your_bot_token>
export TELEGRAM_CHAT_ID=<your_chat_id>
export NOTIFICATIONS_PW=<your_notification_password>
```

# Running the Application

### Development:

```shell
uv run fastapi dev src/main.py
```
### Production:

```shell
uv run fastapi run src/main.py
```

# Interactive API Documentation

http://localhost:8000/docs

# Testing

```bash
uv run pytest
```
or

```bash
uv run pytest tests/api_test.py -v
```

# Example (with curl)
```bash
curl -X POST http://localhost:8000/notifications \
  -H "Content-Type: application/json" \
  -d '{
    "Type": "Warning",
    "Name": "Backup Failure",
    "Description": "The backup failed due to a database problem."
  }'
```
