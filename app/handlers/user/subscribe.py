from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, Text
from loader import dp, bot, _
from app.keyboards.inline_keyboard import sub_ikb

async def check_sub_channel(channel):
    if channel['status'] != 'left':return True


@dp.message_handler(Command('subscribe'))
async def comm_subcribe(message: types.Message):
    if await check_sub_channel(await bot.get_chat_member(chat_id="you_channel_id",user_id=message.from_user.id)):
        await message.answer(
            text=f"Вы подписанны на все каналы!",
        )
    else:
        await message.answer(
            text=_(f"Подпишись на каналы:"),
            reply_markup=await sub_ikb()
        )
@dp.callback_query_handler(text=("sub_check"))
async def check_subscribe( callback: types.CallbackQuery):
    pass