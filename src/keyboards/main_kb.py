from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.settings import MINI_APP_LINK


kb = InlineKeyboardButton(
    text="🔷 Interface",
    web_app={"url": MINI_APP_LINK},
)
keyboard = InlineKeyboardMarkup(inline_keyboard=[[kb]])
