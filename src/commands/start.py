from pyrogram import filters
from pyrogram.types import Message
from src import ADMINS, SERVER_URL
from src.functions.already_join_chat import already_join_chat
from src.functions.force_sub_reply import force_sub_reply
from src.functions.get_invite_link import get_invite_link
from src.functions.send_vid_link import send_vid_link
from src.__main__ import app
from os import environ
import requests


@app.on_message(filters.command("start"))
async def start(client, message: Message):
    if len(message.command) > 1:
        vid_id = message.command[1]
        if message.from_user.id in ADMINS:
            await send_vid_link(vid_id, message.chat.id)
        elif "FORCE_GROUP_ID" in environ and "FORCE_CHANNEL_ID" in environ:
            force_group_id = int(environ.get("FORCE_GROUP_ID"))
            force_channel_id = int(environ.get("FORCE_CHANNEL_ID"))
            group_invitelink = await get_invite_link(force_group_id)
            channel_invitelink = await get_invite_link(force_channel_id)

            already_join_group = await already_join_chat(force_group_id, message.from_user.id)
            already_join_channel = await already_join_chat(force_channel_id, message.from_user.id)

            if already_join_group and already_join_channel:
                await send_vid_link(vid_id, message.chat.id)
            elif already_join_group and not already_join_channel:
                await force_sub_reply(message.from_user, vid_id, None, channel_invitelink)
            elif not already_join_group and already_join_channel:
                await force_sub_reply(message.from_user, vid_id, group_invitelink, None)
            else:
                await force_sub_reply(message.from_user, vid_id, group_invitelink, channel_invitelink)
        elif "FORCE_GROUP_ID" in environ and "FORCE_CHANNEL_ID" not in environ:
            force_group_id = int(environ.get("FORCE_GROUP_ID"))
            group_invitelink = await get_invite_link(force_group_id)
            already_join_group = await already_join_chat(force_group_id, message.from_user.id)

            if already_join_group:
                await send_vid_link(vid_id, message.chat.id)
            else:
                await force_sub_reply(message.from_user, vid_id, group_invitelink, None)
        elif "FORCE_GROUP_ID" not in environ and "FORCE_CHANNEL_ID" in environ:
            force_channel_id = int(environ.get("FORCE_CHANNEL_ID"))
            channel_invitelink = await get_invite_link(force_channel_id)
            already_join_channel = await already_join_chat(force_channel_id, message.from_user.id)

            if already_join_channel:
                await send_vid_link(vid_id, message.chat.id)
            else:
                await force_sub_reply(message.from_user, vid_id, None, channel_invitelink)
        else:
            await send_vid_link(vid_id, message.chat.id)

    requests.post(f"{SERVER_URL}/users/{message.from_user.id}")
