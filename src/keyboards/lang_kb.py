from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


class LangCallback(CallbackData, prefix="my"):
    lang: str
    action: str


settings_ru = InlineKeyboardButton(
    text="Русский",
    callback_data=LangCallback(lang="ru", action="select_lang_settings").pack(),
)
settings_en = InlineKeyboardButton(
    text="English",
    callback_data=LangCallback(lang="en", action="select_lang_settings").pack(),
)
settings_tr = InlineKeyboardButton(
    text="Türkçe",
    callback_data=LangCallback(lang="tr", action="select_lang_settings").pack(),
)
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[settings_ru, settings_en, settings_tr]]
)


main_ru = InlineKeyboardButton(
    text="Русский",
    callback_data=LangCallback(lang="ru", action="select_lang_main").pack(),
)
main_en = InlineKeyboardButton(
    text="English",
    callback_data=LangCallback(lang="en", action="select_lang_main").pack(),
)
main_tr = InlineKeyboardButton(
    text="Türkçe",
    callback_data=LangCallback(lang="tr", action="select_lang_main").pack(),
)
main_lang_keyboard = InlineKeyboardMarkup(inline_keyboard=[[main_ru, main_en, main_tr]])
