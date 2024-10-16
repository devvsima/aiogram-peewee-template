from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType

from loader import dp, bot
from app.filters.admin import Admin
from aiogram.dispatcher.filters.state import StatesGroup, State


class Send(StatesGroup):
    input = State()


@dp.message_handler(Admin(), Command("send"))
async def _admin_command(message: types.Message):
    await message.answer(
        text=f"Напишите сообщение, которое вы хотите отправить всем пользователям. 🥸\n\n/cancel чтобы выйти"
    )
    await Send.input.set()

@dp.message_handler(content_types=ContentType.TEXT, state=Send.input)
async def _send(message: types.Message, state: FSMContext):
    await send_telegram_message(message.text)
    await Send.next()
    
    
async def send_telegram_message(text):
    try:
        await bot.send_message(chat_id="-1002427219718", text=text)
    except:
        ...