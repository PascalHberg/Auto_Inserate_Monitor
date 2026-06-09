import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

MIN_PS = 190
MAX_KM = 150000
MIN_YEAR = 2008
MAX_PRICE = 75000

SCRAPE_INTERVAL = 600
