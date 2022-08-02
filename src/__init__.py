from pyromod import listen
from pyrogram import Client
from dotenv import load_dotenv
from os import getenv
from time import time
import sys

load_dotenv()

if not getenv('API_ID'):
    print('Please provide API_ID')
    sys.exit()
if not getenv('API_HASH'):
    print('Please provide API_HASH')
    sys.exit()
if not getenv('BOT_TOKEN'):
    print('Please provide BOT_TOKEN')
    sys.exit()
if not getenv('ADMINS'):
    print('Please provide at least one ADMIN')
    sys.exit()
if not getenv('DSTREAM_API_KEY'):
    print('Please provide DSTREAM_API_KEY')
    sys.exit()
if not getenv('SERVER_URL'):
    print('Please provide SERVER_URL')
    sys.exit()
if not getenv('CHANNEL_ID'):
    print('Please provide CHANNEL_ID')
    sys.exit()

API_ID = int(getenv('API_ID'))
API_HASH = getenv('API_HASH')
BOT_TOKEN = getenv('BOT_TOKEN')
ADMINS = list(map(int, getenv('ADMINS').split()))
START_TIME = time()
DSTREAM_API_KEY = getenv("DSTREAM_API_KEY")
SERVER_URL = getenv("SERVER_URL")
CHANNEL_ID = int(getenv("CHANNEL_ID"))


class RK73(Client):
    def __init__(self):
        super().__init__('rk73', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

    async def start(self):
        await super().start()
        me = await self.get_me()

        print(f"App started as {me.username}")


app = RK73()
