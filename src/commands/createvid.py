from pyrogram import filters
from pyrogram.types import Message
from src import ADMINS, SERVER_URL
from src.__main__ import app
from src.functions.autopostch import autopostch
from src.functions.upload_vid import upload_vid
import requests


@app.on_message(filters.command("createvid"))
async def createvid(client, message: Message):
    if message.from_user.id in ADMINS:
        answer = await app.ask(chat_id=message.chat.id, text='Send the video you want to posted')
        while answer.video is None:
            answer = await app.ask(chat_id=message.chat.id, text='Please provide the right vid')
            if answer.video:
                break
        vid_hash = answer.video.file_id
        answer = await app.ask(chat_id=message.chat.id, text="Now input the name of the video")
        while answer.text is None:
            answer = await app.ask(chat_id=message.chat.id, text="Please provide the right name")
            if answer.text:
                break
        vid_name = answer.text
        answer = await app.ask(chat_id=message.chat.id, text="Send the image preview of the vid")
        while answer.photo is None:
            answer = await app.ask(chat_id=message.chat.id, text="Please provide the right picture")
            if answer.photo:
                break

        # Photos in Pyogram is not the same as photos in Telegraf
        # Pyogram only has 1 photo and thumbs
        # that's why we don't access it with list
        vid_image = answer.photo.file_id

        wait_message = await message.reply("<code>Trying to download</code>")
        await app.download_media(vid_hash, f"{vid_name}.mp4")
        await wait_message.edit("<code>Generate vid link..</code>")
        dstream_response = upload_vid(f"./downloads/{vid_name}.mp4")
        vid_link = dstream_response["result"][0]["download_url"]
        await wait_message.edit("<code>Saving into database</code>")
        db_response = requests.post(
            f"{SERVER_URL}/vids", json={"name": vid_name, "image": vid_image, "hash": vid_hash, "link": vid_link}).json()
        await wait_message.edit("<code>Posts into channel</code>")
        await autopostch(db_response)
        await wait_message.delete()
        await message.reply(f"<strong>ID:</strong> <code>{db_response['id']}</code>\n<strong>Name:</strong> <code>{db_response['name']}</code>\n<strong>Link:</strong> {db_response['link']}", disable_web_page_preview=True)
    else:
        await message.reply("Maaf, fitur ini hanya untuk admin")
