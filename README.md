# 🛒 Walmart Inventory Discord Bot

This is a Discord bot that searches Walmart for product availability using a UPC and ZIP code.

## 🔧 Features

- Slash-style command `/walmart <upc> <zip>`
- Retrieves Walmart product titles using UPC
- Works with a headless Chrome browser via Selenium

## 🚀 Setup Instructions

1. Clone the repo:
    ```bash
    git clone https://github.com/yourusername/walmart-bot.git
    cd walmart-bot
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `config.py` file:
    ```python
    TOKEN = "your-discord-bot-token"
    ```

4. Make sure you have Chrome and `chromedriver` installed.
   - Download from: https://sites.google.com/a/chromium.org/chromedriver/

5. Run the bot:
    ```bash
    python bot.py
    ```

## ⚠️ Notes

- Walmart's site may change or block automated bots.
- Results may vary based on region and scraping limitations.
- Never commit your `config.py` or bot token.

## 📄 License

MIT License