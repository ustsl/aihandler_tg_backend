from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from src.settings import MINI_APP_LINK

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🔷 Interface",
                web_app={"url": MINI_APP_LINK},
            )
        ],
    ],
    input_field_placeholder="Menu",
)


kb = InlineKeyboardButton(
    text="🔷 Interface",
    web_app={"url": MINI_APP_LINK},
)
main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔷 Interface",
                web_app={"url": MINI_APP_LINK},
            )
        ]
    ]
)
