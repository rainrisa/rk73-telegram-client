from src import app


async def get_invite_link(chat_id):
    chat = await app.get_chat(chat_id)
    invitelink = chat.invite_link

    if invitelink is None:
        invitelink = await app.export_chat_invite_link(chat_id)

    return invitelink
