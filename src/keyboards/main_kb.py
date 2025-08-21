from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MainCallback(CallbackData, prefix="my"):
    command: str
    action: str


from src.settings import MINI_APP_LINK, SUBSCRIPTION_PRICE


kb = InlineKeyboardButton(
    text="🔷 Interface",
    web_app={"url": MINI_APP_LINK},
)

reverse = InlineKeyboardButton(
    text="Вернуться назад",
    callback_data=MainCallback(command="main", action="reverse").pack(),
)


def payment_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text=f"Оплатить {SUBSCRIPTION_PRICE} ⭐️", pay=True)

    return builder.as_markup()


payment = InlineKeyboardButton(
    text=f"Пополнить баланс ⭐️",
    callback_data=MainCallback(command="main", action="payment").pack(),
)


keyboard = InlineKeyboardMarkup(inline_keyboard=[[kb], [payment]])

reverse_kb = InlineKeyboardMarkup(inline_keyboard=[[reverse]])
