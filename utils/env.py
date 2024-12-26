from environs import Env


env = Env()
env.read_env()


BOT_TOKEN = env('BOT_TOKEN')
WEBAPP_URL = env('WEBAPP_URL')
BASE_URL = env('BASE_URL')
CHANNEL_ID = env('GROUP_ID')