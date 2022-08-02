from pyrogram.types import User, InlineKeyboardMarkup, InlineKeyboardButton
from src import app


async def force_sub_reply(user: User, vid_id, force_group_link, force_channel_link):
    me = await app.get_me()
    reply_message = f"Hello {user.first_name}\n\nAnda harus bergabung di Channel/Grup dibawah untuk menggunakan saya\n\nSilakan Join Terlebih Dahulu"
    group_icon = "💠 Join Grup"
    channel_icon = "🔰 Join Channel"
    try_again_icon = "🥤 Try Again"
    try_again_link = f"https://t.me/{me.username}?start={vid_id}"

    if force_group_link and force_channel_link:
        await app.send_message(chat_id=user.id, text=reply_message, reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(text=group_icon, url=force_group_link),
                InlineKeyboardButton(text=channel_icon, url=force_channel_link)
            ],
            [
                InlineKeyboardButton(text=try_again_icon, url=try_again_link)
            ]
        ]))
    if force_group_link and not force_channel_link:
        await app.send_message(chat_id=user.id, text=reply_message, reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(text=group_icon, url=force_group_link)
            ],
            [
                InlineKeyboardButton(text=try_again_icon, url=try_again_link)
            ]
        ]))
    if not force_group_link and force_channel_link:
        await app.send_message(chat_id=user.id, text=reply_message, reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(text=channel_icon, url=force_channel_link)
            ],
            [
                InlineKeyboardButton(text=try_again_icon, url=try_again_link)
            ]
        ]))
