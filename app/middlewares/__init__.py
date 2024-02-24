from aiogram import Dispatcher
from .user import UsersMiddleware
from .throttling import TrottlingMiddleware
from .i18n import I18nMiddleware


def setup_middlewares(dp: Dispatcher) -> None:
    dp.middleware.setup(UsersMiddleware())
    # dp.middleware.setup(TrottlingMiddleware())
    # dp.middleware.setup(I18nMiddleware)