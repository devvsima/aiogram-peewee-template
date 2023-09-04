from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
from loader import dp, bot

# from utils.misc import rate_limit


# @rate_limit(5, key="start")
@dp.message_handler(CommandStart())
async def comm_start(message: types.Message):
    await message.answer(
        text=f"Добро пожаловать",
    )
