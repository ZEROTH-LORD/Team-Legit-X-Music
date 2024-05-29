from LEGITMUSIC import legitdb


async def put(
    chat_id,
    title,
    duration,
    videoid,
    file_path,
    ruser,
    user_id,
):
    put_f = {
        "title": title,
        "duration": duration,
        "file_path": file_path,
        "videoid": videoid,
        "req": ruser,
        "user_id": user_id,
    }
    get = legitdb.get(chat_id)
    if get:
        legitdb[chat_id].append(put_f)
    else:
        legitdb[chat_id] = []
        legitdb[chat_id].append(put_f)
