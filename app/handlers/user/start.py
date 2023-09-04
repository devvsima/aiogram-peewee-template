from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
from loader import dp, bot


@dp.message_handler(CommandStart())
async def comm_start(message: types.Message):
    await message.answer(
        text=f"Добро пожаловать",
    )
