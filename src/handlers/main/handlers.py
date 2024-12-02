from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import F, Router

from src.actions.user.base import get_or_create_user


from src.actions.user.settings import update_language

from src.keyboards.main_kb import keyboard as kb
from src.keyboards.lang_kb import LangCallback, main_lang_keyboard
from src.messages.base import start_message


from aiogram.types import Message, CallbackQuery

from aiogram import F, Router


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
    result = await get_or_create_user(message.from_user.id)
    current_lang = result.get("settings").get("language")
    if not current_lang:
        await message.answer("Select language", reply_markup=main_lang_keyboard)
    else:
        msg = start_message(
            user=message.from_user.full_name,
            balance=result.get("accounts").get("balance"),
            language=current_lang,
        )
        await message.answer(msg, reply_markup=kb)


@router.callback_query(LangCallback.filter(F.action == "select_lang_main"))
async def language_callback(query: CallbackQuery, callback_data: LangCallback):
    lang = str(callback_data.lang).lower()
    user = str(query.from_user.id)
    await update_language(user=user, lang=lang)
    result = await get_or_create_user(user)
    msg = start_message(
        user="", balance=result.get("accounts").get("balance"), language=lang
    )
    await query.message.answer(msg, reply_markup=kb)
