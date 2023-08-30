from aiogram import types, Dispatcher
from loader import dp, bot


@dp.message_handler(commands=["start"])
async def comm_start(message: types.Message):
    await message.answer(
        text="Добро пожаловать",
    )
