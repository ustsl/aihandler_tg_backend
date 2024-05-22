from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router

from src.actions.query.base import post_query
from src.actions.user.base import get_or_create_user, get_user
from src.api.requests import put_request
from src.fsm.query import QueryState
from src.keyboards.keyboard import main as kb
from src.messages.base import about_message, start_message

from aiogram.fsm.context import FSMContext


from src.settings import API_DOMAIN, API_MAIN_TOKEN

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    result = await get_or_create_user(message.from_user.id)
    msg = start_message(
        user=message.from_user.full_name, balance=result.get("accounts").get("balance")
    )
    await message.answer(msg, reply_markup=kb)


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


@router.message(Command("about"))
async def clear_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(QueryState.story)
    await state.clear()
    msg = about_message()
    await message.answer(msg, reply_markup=kb)


@router.message(QueryState.wait)
async def wait_handler(message: Message, state: FSMContext) -> None:
    await message.answer(
        "Wait. Everything is fine - the request is being processed.", parse_mode=None
    )


@router.message(F.text)
async def post_query_handler(message: Message, state: FSMContext) -> None:
    try:
        # SET state process
        await state.set_state(QueryState.wait)

        # Get story data
        data = await state.get_data()
        old_story = []
        if data.get("story"):
            old_story = data.get("story")

        user = await get_user(message.from_user.id)
        prompt_id = user.get("settings").get("prompt_id")
        token = user.get("token").get("token")

        await message.answer("The request is being processed..", parse_mode=None)

        result = await post_query(
            telegram_id=message.from_user.id,
            prompt_id=prompt_id,
            query=message.text,
            token=token,
            story=old_story,
        )

        if result.get("detail"):
            msg = result.get("detail")
        else:
            msg = result.get("result")
            # Update story data
            current_story = [
                {"role": "user", "content": message.text},
                {"role": "system", "content": result.get("clean")},
            ]
            new_story = [*old_story, *current_story][-30:]  # 30 - limit
            await state.set_state(QueryState.story)
            await state.update_data(story=new_story)
        if msg:
            await message.answer(msg, reply_markup=kb, parse_mode=None)
        else:
            await message.answer("Error")
    except Exception as e:
        await state.clear()
        await message.answer(
            "Error. Try clearing your message history using the /clear command and try again."
        )
