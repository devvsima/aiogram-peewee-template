from aiogram import types, Dispatcher
from loader import dp, bot, _
from aiogram.dispatcher.filters import CommandSettings

@dp.message_handler(commands="Настройки⚙️")
@dp.message_handler(CommandSettings())
async def comm_start(message: types.Message):
    await message.answer(
        text=_("Настройки⚙️"),
    )
