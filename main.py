from aiogram import Dispatcher, executor
from database import *
from app import middlewares, filters, handlers
from loader import dp, bot
from utils.misc.logging import *


async def on_startup(_):
    print(" [On_startup] ")


async def on_shutdown(dispatcher: Dispatcher):
    print("Shutting down...")


if __name__ == "__main__":
    executor.start_polling(     
        dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
    )
