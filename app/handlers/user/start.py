from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp, bot, _

@dp.message_handler(CommandStart())
async def _start_command(message: types.Message):
    text = _(f"👋, <a href='tg://user?id={message.from_user.id}'>{(message.from_user.full_name)}</a>")
    await message.answer(text)
