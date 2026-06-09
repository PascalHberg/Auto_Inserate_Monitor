import requests
from config import BOT_TOKEN, CHAT_ID

class TelegramService:
    def __init__(self, logger):
        self.logger = logger

    def send(self, text: str):
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": CHAT_ID,
            "text": text,
            "disable_web_page_preview": True
        }

        try:
            requests.post(url, data=payload, timeout=10)
        except Exception as e:
            self.logger.error(f"Telegram Fehler: {e}")
