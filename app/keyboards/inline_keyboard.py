from aiogram.types import (
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


async def base_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Название", callback_data="callback"),
            ],
        ],
    )
    return ikb

async def sub_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Канал 1", url="https://t.me/+7lZSbqjjRHEwOGMy"),
            ],
            [
                InlineKeyboardButton(text="Проверить", callback_data="sub_check"),
            ],
        ],
    )
    return ikb

