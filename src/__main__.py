from pyrogram import idle
from asyncio import get_event_loop
from importlib import import_module
from src.commands import ALL_COMMANDS
from src import app


loop = get_event_loop()


async def init():
    await app.start()
    for command in ALL_COMMANDS:
        import_module("src.commands." + command)
    await idle()

if __name__ == "__main__":
    loop.run_until_complete(init())
