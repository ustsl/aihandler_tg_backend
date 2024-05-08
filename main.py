#!/usr/bin/env python3


import asyncio
import logging
import sys


from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# from src.settings import BOT_TOKEN

from src.handlers.base import router as base_router


BOT_TOKEN = "6560303286:AAH1DraNhX-j5mzx8hD6o77WssGEMqEVwK8"

dp = Dispatcher()
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def main() -> None:
    dp.include_router(base_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
