import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode

from config import settings
from database import create_users_table

from routers import router as main_router


async def main():
    try:
        create_users_table()
    except Exception:
        print("Table have existed yet!")

    dp = Dispatcher()

    dp.include_router(main_router)


    logging.basicConfig(level=logging.INFO)

    bot = Bot(
        token=settings.bot_token,
        parse_mode=ParseMode.HTML
    )

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
