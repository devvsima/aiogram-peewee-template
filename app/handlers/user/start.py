from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
from loader import dp, bot
from config.config import admins

@dp.message_handler(user_id=admins, commands="start")
async def comm_start(message: types.Message):
    await message.answer(
        text=f"Добро пожаловать",
    )
