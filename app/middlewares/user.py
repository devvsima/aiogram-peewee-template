from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery, InlineQuery

from database.service.users import get_or_create_user


class UsersMiddleware(BaseMiddleware):
    @staticmethod
    async def on_process_message(message: Message, data: dict[str]):
        print(message)
        if message.chat.type == "supergroup":
            print("1")
        elif 'channel_post' in message or message.chat.type != 'private':
            raise CancelHandler()

        await message.answer_chat_action('typing')

        user = message.from_user

        data['user'] = get_or_create_user(user.id, user.username)

    @staticmethod
    async def on_process_callback_query(callback_query: CallbackQuery, data: dict[str]):
        user = callback_query.from_user

        data['user'] = get_or_create_user(user.id, user.username)

    @staticmethod
    async def on_process_inline_query(inline_query: InlineQuery, data: dict[str]):
        user = inline_query.from_user

        data['user'] = get_or_create_user(user.id, user.username)