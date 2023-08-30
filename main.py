# aiogram
from aiogram import Dispatcher, executor, types

# my scripts
from database import *
from app import *


from loader import dp, bot


async def on_startup(_):
    print(" [ Бот запущен ] ")


async def on_shutdown(dispatcher: Dispatcher):
    print("Shutting down..")


if __name__ == "__main__":
    executor.start_polling(
        dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
    )
