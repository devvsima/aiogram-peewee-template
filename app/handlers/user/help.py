from aiogram import types, Dispatcher
from loader import dp, bot, _
from aiogram.dispatcher.filters import CommandHelp


@dp.message_handler(commands="Помощь🆘")
@dp.message_handler(CommandHelp())
async def comm_start(message: types.Message):
    await message.answer(
        text=_("Описание"),
    )
