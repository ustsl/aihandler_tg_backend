from dotenv import load_dotenv
from os import getenv

SUBSCRIPTION_PRICE = 100

STARS_PRICE = 0.013


load_dotenv()

API_DOMAIN = "https://imvo.qspk.me/"
BOT_TOKEN = getenv("BOT_TOKEN")
# BOT_TOKEN = getenv("BOT_TOKEN_TEST")


API_MAIN_TOKEN = getenv("API_MAIN_TOKEN")

HEADERS = {"Authorization": API_MAIN_TOKEN}

MINI_APP_LINK = "https://aihandler.imvo.site"
