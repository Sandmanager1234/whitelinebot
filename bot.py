import os
import sys
import asyncio
import logging

from aiogram import Bot, Dispatcher
# from aiogram.enums import ParseMode
# from aiogram.client.default import DefaultBotProperties

from dispatcher import get_dp
from classes.db_manager import ManagerBD


TOKEN = os.getenv('BOT_TOKEN')
DBNAME = os.getenv('DB_NAME')
USERNAME = os.getenv('DB_USERNAME')
USER_PASSWORD = os.getenv('DB_USERNAME_PASSWORD')

db_manager = ManagerBD(dbname=DBNAME, dbuser=USERNAME, user_password=USER_PASSWORD)


async def main() -> None:

    dp = get_dp()
    bot = Bot(
        token=TOKEN,
        # default=DefaultBotProperties(parse_mode=ParseMode)
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
