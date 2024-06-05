from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from aiogram import F, Router

from src.actions.user.base import get_or_create_user
from src.actions.user.settings import update_language
from src.api.requests import put_request
from src.fsm.query import QueryState
from src.keyboards.main_kb import keyboard as kb
from src.keyboards.lang_kb import LangCallback, keyboard as kb_lang
from src.messages.base import about_message

from aiogram.fsm.context import FSMContext

from src.settings import API_DOMAIN, API_MAIN_TOKEN
from src.messages.tech import language_message

router = Router()


@router.message(Command("clear"))
async def clear_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(QueryState.story)
    await state.clear()
    await message.answer("Message story has been deleted", reply_markup=kb)


@router.message(Command("refresh_token"))
async def clear_handler(message: Message) -> None:
    url = f"{API_DOMAIN}v1/users/{str(message.from_user.id)}/token"
    await put_request(url=url, headers={"Authorization": API_MAIN_TOKEN})
    await message.answer("Token was refreshed", reply_markup=kb)


@router.message(Command("language"))
async def select_language_handler(message: Message) -> None:
    await message.answer("Select language", reply_markup=kb_lang)


@router.callback_query(LangCallback.filter(F.action == "select_lang_settings"))
async def language_callback(query: CallbackQuery, callback_data: LangCallback):
    lang = str(callback_data.lang).lower()
    await update_language(user=str(query.from_user.id), lang=lang)
    await query.message.answer(language_message.get(lang), reply_markup=kb)


@router.message(Command("about"))
async def clear_handler(message: Message, state: FSMContext) -> None:
    print(312312312321312312)
    user = await get_or_create_user(message.from_user.id)
    print(user)
    current_lang = (user.get("settings")).get("language")
    await state.set_state(QueryState.story)
    await state.clear()
    if not current_lang:
        current_lang = "en"
    msg = about_message.get(current_lang)
    await message.answer(msg, reply_markup=kb)
