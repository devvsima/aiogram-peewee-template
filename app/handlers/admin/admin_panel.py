from aiogram import types, Dispatcher
from loader import dp, bot
from config.config import admins

@dp.message_handler(user_id=admins, commands="admin")
async def comm_start(message: types.Message):
    await message.answer(
        text=f"Вы админ"
    )
