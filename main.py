#!/usr/bin/env python3


import asyncio
import logging
import sys


from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.settings import BOT_TOKEN

from src.handlers.main.handlers import router as main_router
from src.handlers.tech.handlers import router as tech_router
from src.handlers.query.handlers import router as query_router
from src.handlers.payment.handlers import router as payment_router

dp = Dispatcher()
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def main() -> None:
    dp.include_router(main_router)
    dp.include_router(tech_router)
    dp.include_router(query_router)
    dp.include_router(payment_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
