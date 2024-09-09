from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command

from loader import dp, _
from app.filters.admin import Admin


@dp.message_handler(Admin(), Command("admin"))
async def _admin_command(message: types.Message):
    await message.answer(
        text=_("You admin!")
    )
