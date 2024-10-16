

from aiogram import types


from aiogram.utils.callback_data import CallbackData

whisper_callback = CallbackData("whisper", "msg_id")

async def generate_button(id):
    button = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Press button",
                    callback_data=whisper_callback.new(
                        msg_id = id
                    )
                )
            ]
        ]
    )

    return button