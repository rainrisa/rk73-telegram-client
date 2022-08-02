from src import app
from pyrogram.enums.chat_member_status import ChatMemberStatus


async def already_join_chat(chat_id, user_id):
    try:
        user = await app.get_chat_member(int(chat_id), user_id)
        if user.status == ChatMemberStatus.LEFT or user.status == ChatMemberStatus.BANNED:
            return False
        else:
            return True
    except:
        return False
