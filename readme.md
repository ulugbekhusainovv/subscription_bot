# SubscriptionBot

Mandatory Subscription Bot

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Mandatory subscription bot this project is written in Version 3 of aiogram

## Installation

Follow these steps to install and run the project:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ulugby/subscription_bot.git
    cd your_project_name
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up environment variables**:
    - Create a new `.env` file in the project root:
    ```bash
    touch .env
    ```
    - Add your bot's token and admin details:
    ```bash
    BOT_TOKEN=your_bots_token
    ADMINS=your_telegram_id
    ```

6. **Run the application**:
    ```bash
    python app.py
    ```

7. **Access the bot**:
    - Open Telegram and interact with the bot at `@your_bot_username`.

## Configuration

You can configure the bot by editing the `.env` file and adding relevant parameters. Make sure to replace the placeholder values with your actual bot's token and administrator ID.

```bash
BOT_TOKEN=your_bots_token
ADMINS=your_telegram_id
