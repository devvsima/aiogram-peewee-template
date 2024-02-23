from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp, bot, _
from database.service import add_user

@dp.message_handler(CommandStart())
async def _start_command(message: types.Message):
    text = _(f"👋, <a href='tg://user?id={message.from_user.id}'>{(message.from_user.full_name)}</a>")
    add_user(message.from_user.id)
    await message.answer(text)
