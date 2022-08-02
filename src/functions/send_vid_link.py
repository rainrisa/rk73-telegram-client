from src import app, SERVER_URL
import requests


async def send_vid_link(vid_id, chat_id):
    try:
        data = requests.get(f"{SERVER_URL}/vids/{vid_id}").json()
        await app.send_message(int(chat_id), data["link"])
        requests.post(f"{SERVER_URL}/vids/{vid_id}/click")
        requests.post(f"{SERVER_URL}/users/{chat_id}/updateClick")
    except Exception as err:
        print(err)
        await app.send_message(int(chat_id), "Vid tidak ditemukan")
