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
        
from random import randrange
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def podeb(message: types.Message):
    rand = randrange(1, 4)
    if rand == 1:
        if "коля лох" == message.text.lower(): await message.reply("факт")
        elif "лох" == message.text.lower(): await message.reply("коля?")
        elif "да" == message.text.lower() == "да": await message.reply("пизда")
        elif "ирис" in message.text.lower(): await message.reply("🔪")
    # elif "будешь завтра?" in message.text.lower(): await message.reply("я буду🥰")
import uuid
from app.keyboards.inline.generator import generate_button
@dp.inline_handler()
async def inline(query: types.InlineQuery):
    text = query.query

    lst = text.split("||")

    txt_len = len(text)

    if len(lst) >= 2:
        as_len = len(lst[1])
    else:
        as_len = 0

    if len(lst) >= 2 and txt_len<=255 and as_len<200:

        #print(text)
        msg_id = str(uuid.uuid4())


        button = await generate_button(msg_id)



        result = types.InlineQueryResultArticle(
            id=msg_id,
            title=f"Whisper Message | {len(lst[1])}/200 | {txt_len}/255",
            input_message_content=types.InputTextMessageContent(
                message_text="New message",
            ),
            reply_markup=button,
        )

        await query.answer(results=[result,])
    else:


        result = types.InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title=f"Yaroqsiz Xabar | {as_len}/200 | {txt_len}/255",
            input_message_content=types.InputTextMessageContent(
                message_text="New message",
            )
        )

        await query.answer(results=[result,])