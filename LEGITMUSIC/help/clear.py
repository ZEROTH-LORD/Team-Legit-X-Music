from LEGITMUSIC import legitdb
from LEGITMUSIC.help import remove_active_chat


async def _clear_(chat_id):
    try:
        legitdb[chat_id] = []
        await remove_active_chat(chat_id)
    except:
        return
