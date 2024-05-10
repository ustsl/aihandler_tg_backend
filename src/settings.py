from dotenv import load_dotenv
from os import getenv

load_dotenv()

API_DOMAIN = "https://aihandler.qsbot.app/"
BOT_TOKEN = getenv("BOT_TOKEN")
API_MAIN_TOKEN = getenv("API_MAIN_TOKEN")

HEADERS = {"Authorization": API_MAIN_TOKEN}

MINI_APP_LINK = "https://aihandler.imvo.site"
