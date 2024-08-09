from aiogram import Router, types
from aiogram.filters import CommandStart

from bot import db_manager
from templates import TEMPLATES
from filters import AdminFilter

start_router = Router()

# dp.include_router(start_router)

@start_router.message(AdminFilter(), CommandStart())
async def command_start_handler(msg: types.Message) -> None:
    if not db_manager.user_exist(msg.from_user.id):
        user = msg.from_user
        db_manager.add_user(user)
    await msg.answer(TEMPLATES['welcome_admin'].format(msg.from_user.first_name))


@start_router.message(CommandStart())
async def command_start_handler(msg: types.Message) -> None:
    if not db_manager.user_exist(msg.from_user.id):
        user = msg.from_user
        db_manager.add_user(user)
    await msg.answer(TEMPLATES['welcome'].format(msg.from_user.first_name))
