from src import START_TIME
from pyrogram import filters
from pyrogram.types import Message
from src.__main__ import app
from time import time
import math


@app.on_message(filters.command("uptime"))
async def uptime(client, message: Message):
    uptime_total = round(time() - START_TIME)
    uptime_hours = math.floor(uptime_total / 3600)
    uptime_total -= uptime_hours * 3600
    uptime_minutes = math.floor(uptime_total / 60)
    uptime_total -= uptime_minutes * 60
    uptime_seconds = uptime_total

    if uptime_hours != 0 and uptime_minutes != 0:
        await message.reply(f"{uptime_hours}h {uptime_minutes}m {uptime_seconds}s")
    elif uptime_hours == 0 and uptime_minutes != 0:
        await message.reply(f"{uptime_minutes}m {uptime_seconds}s")
    else:
        await message.reply(f"{uptime_seconds}s")
