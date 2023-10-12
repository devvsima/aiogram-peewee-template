from pathlib import Path

from environs import Env

env = Env()
env.read_env()


DIR = Path(__file__).absolute().parent.parent

token_api = env.str("TOKEN", default=None)
banned_users = [env("BANED", default=None)]
admins = [env("ADMINS", default=None)]
mongodb_url = [env("MONGODB_URL", default=None)]

I18N_DOMAIN = 'bot'
LOCALES_DIR = f'{DIR}\config\locales'

