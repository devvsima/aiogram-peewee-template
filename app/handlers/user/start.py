from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp, bot, _

@dp.message_handler(CommandStart())
async def _start_command(message: types.Message):
    text = _("👋, <a href='tg://user?id={}'>{}</a>")
    await message.answer(text.format(message.from_user.id, message.from_user.full_name))
