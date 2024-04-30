from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔷 Interface", web_app={"url": "https://bot.imvo.site"})],
    ],
    resize_keyboard=True,
    input_field_placeholder="Menu",
)
