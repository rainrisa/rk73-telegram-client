from src import CHANNEL_ID, app


async def autopostch(db_response):
    vid_id = db_response["id"]
    vid_name = db_response["name"]
    vid_image = db_response["image"]
    me = await app.get_me()

    await app.send_photo(CHANNEL_ID, vid_image, f"<strong>Nama:</strong> <code>{vid_name}.mp4</code>\n\n<strong>Link Download:</strong> <a href='https://t.me/{me.username}?start={vid_id}'>Klik Disini</a>")
