from pathlib import Path
from environs import Env

DIR = Path(__file__).absolute().parent.parent

env = Env()
env.read_env()

#  tgbot
token_api = env.str("TOKEN", default=None)
banned_users = env.list("BANED", default=None, subcast=int)
admins = env.list("ADMINS", default=None, subcast=int)

# db
DB_HOST = env.str("DB_HOST", default="localhost")
DB_PORT = env.int("DB_PORT", default=27017)
DB_USER = env.str("DB_USER", default="")
DB_PASS = env.str("DB_PASS", default="")
AUTH_SOURCE = env.str("AUTH_SOURCE", default='admin')
RATE_LIMIT = env.int("RATE_LIMIT", default=5)

if not DB_HOST:
    mongodb_url = f'mongodb://localhost:{DB_PORT}/'
else:
    mongodb_url = f"mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{AUTH_SOURCE}"


I18N_DOMAIN = 'bot'
LOCALES_DIR = f'{DIR}\config\locales'

