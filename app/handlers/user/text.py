from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot, _
import asyncio


@dp.message_handler(Text(["казнь", "Казнь"]))
async def handle_message(message: types.Message):
    if message.from_user.id == 1095614174:
        await message.reply(f"🙄🙄🙄")
        return
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        
        # Мутимо користувача
        await message.chat.restrict(user_id, permissions=types.ChatPermissions(can_send_messages=False))
        await message.reply(f"👉🏼 { message.reply_to_message.from_user.username} на минуту замутили🤯🤯🤯")
        
        # Чекаємо 60 секунд
        await asyncio.sleep(60)
        
        # Знімаємо мутацію
        await message.chat.restrict(user_id, permissions=types.ChatPermissions(can_send_messages=True))
    else:
        await message.reply("не работет магия🤌🏽")

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def kolya(message: types.Message):
    if "коля лох" == message.text.lower(): await message.reply("факт")
    elif "лох" == message.text.lower(): await message.reply("коля?")
    elif "да" == message.text.lower() == "да": await message.reply("пизда")
    elif "ирис" in message.text.lower(): await message.reply("🔪")
    # elif "будешь завтра?" in message.text.lower(): await message.reply("я буду🥰")
