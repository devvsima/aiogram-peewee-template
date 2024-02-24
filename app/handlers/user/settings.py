from aiogram import types
from aiogram.dispatcher.filters import CommandSettings, Command

from loader import dp, bot, _


@dp.message_handler(Command("Settings ⚙️"))
@dp.message_handler(CommandSettings())
async def _settings_command(message: types.Message):
    await message.answer(
        text=_("You settings ⚙️"),
    )
