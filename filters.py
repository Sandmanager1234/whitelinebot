from aiogram.types import Message
from aiogram.filters import BaseFilter


from bot import db_manager


class AdminFilter(BaseFilter):
    def __init__(self) -> None:
        self.admins = db_manager.get_stuff()
    
    async def __call__(self, msg: Message) -> bool:
        # print((msg.from_user.id,) in self.admins)
        return (msg.from_user.id,) in self.admins