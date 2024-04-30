import asyncio
import logging
import sys


from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.settings import BOT_TOKEN

from src.handlers.base import router as base_router

dp = Dispatcher()
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

# Загрузка переменных среды из файла .env


# Bot token can be obtained via https://t.me/BotFather


# All handlers should be attached to the Router (or Dispatcher)


async def main() -> None:
    dp.include_router(base_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
