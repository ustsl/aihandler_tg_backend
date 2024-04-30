from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Dispatcher, html, Router

from src.actions.query.base import post_query
from src.actions.user.base import get_or_create_user, get_user
from src.api.requests import post_request
from src.keyboards.keyboard import main as kb
from src.messages.base import start_message

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    result = await get_or_create_user(message.from_user.id)

    msg = start_message(
        user=message.from_user.full_name, balance=result.get("accounts").get("balance")
    )

    await message.answer(msg)


@router.message()
async def post_query_handler(message: Message) -> None:
    try:
        user = await get_user(message.from_user.id)
        prompt_id = user.get("settings").get("prompt_id")
        token = user.get("token").get("token")
        result = await post_query(
            telegram_id=message.from_user.id,
            prompt_id=prompt_id,
            query=message.text,
            token=token,
        )
        msg = result.get("result")
        if msg:
            await message.answer(msg, reply_markup=kb)
        else:
            await message.answer("Error")
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")
