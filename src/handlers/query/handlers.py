from aiogram.types import Message
from aiogram import F, Router

from src.actions.query.base import post_query
from src.actions.user.base import get_user

from src.fsm.query import QueryState
from src.keyboards.main_kb import keyboard as kb


from aiogram.fsm.context import FSMContext

import io
import aiohttp


from src.modules.filestorage.action import FileStorageAction
from src.settings import API_MAIN_TOKEN


router = Router()


@router.message(QueryState.wait)
async def wait_handler(message: Message, state: FSMContext) -> None:
    await message.answer(
        "Wait. Everything is fine - the request is being processed.", parse_mode=None
    )


# Need refactoting
@router.message(F.photo)
async def image_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(QueryState.start)
    try:
        # SET state process
        await state.set_state(QueryState.wait)

        file_id = message.photo[-1].file_id
        file = await message.bot.get_file(file_id)
        file_path = file.file_path
        file_data = await message.bot.download_file(file_path)
        photo_bytes = io.BytesIO(file_data.getvalue())

        # URL и headers для POST-запроса

        headers = {"Authorization": API_MAIN_TOKEN}
        path = None
        is_downloaded = False
        # Отправка POST-запроса с фото

        url = f"https://filestorage.imvo.site/v1/files/image/{message.from_user.id}"

        filestorage_action = FileStorageAction()
        download_result = await filestorage_action.download(url=url, file=photo_bytes)
        path = download_result.get("path")
        is_downloaded = download_result.get("is_downloaded")

        if is_downloaded:
            query = f"https://filestorage.imvo.site/v1/files/?path={path}"
            user = await get_user(message.from_user.id)
            prompt_id = user.get("settings").get("prompt_id")
            token = user.get("token").get("token")
            await message.answer("The request is being processed..", parse_mode=None)

            result = await post_query(
                telegram_id=message.from_user.id,
                prompt_id=prompt_id,
                query=query,
                token=token,
                story=[],
                vision=True,
            )

            if result.get("detail"):
                msg = result.get("detail")
            else:
                msg = result.get("result")

            if msg:
                await message.answer(msg, reply_markup=kb, parse_mode=None)
            else:
                await message.answer("Error")

            async with aiohttp.ClientSession() as session:
                async with session.delete(query, headers=headers) as delete_response:
                    if delete_response.status == 200:
                        print("File deleted successfully")
                    else:
                        print("Failed to delete file")

        await state.clear()

    except Exception as e:
        print(e)
        await state.clear()
        await message.answer(
            "Error. Try clearing your message history using the /clear command and try again."
        )


# Need refactoting
@router.message(F.text)
async def post_query_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(QueryState.start)
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
            vision=False,
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
        await message.answer(str(e))
        await message.answer(
            "Error. Try clearing your message history using the /clear command and try again."
        )
