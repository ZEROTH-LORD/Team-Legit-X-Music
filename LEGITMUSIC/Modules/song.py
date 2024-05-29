import os

import requests
import yt_dlp
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch

from LEGITMUSIC import BOT_MENTION, BOT_USERNAME, LOGGER, app


@app.on_message(filters.command(["song", "vsong", "video", "music"]))
async def song(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    m = await message.reply_text("🔎")

    query = "".join(" " + str(i) for i in message.command[1:])
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=5).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as ex:
        LOGGER.error(ex)
        return await m.edit_text(
            f"ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴛʀᴀᴄᴋ ғʀᴏᴍ ʏᴛ-ᴅʟ.\n\n**ʀᴇᴀsᴏɴ :** `{ex}`"
        )

    await m.edit_text("» ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ sᴏɴɢ,\n\nᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"☁️ **ᴛɪᴛʟᴇ :** [{title[:23]}]({link})\n⏱️ **ᴅᴜʀᴀᴛɪᴏɴ :** `{duration}`\n🥀 **ᴜᴘʟᴏᴀᴅᴇᴅ ʙʏ :** {BOT_MENTION}"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
        try:
            visit_butt = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ʏᴏᴜᴛᴜʙᴇ",
                            url=link,
                        )
                    ]
                ]
            )
            await app.send_audio(
                chat_id=message.from_user.id,
                audio=audio_file,
                caption=rep,
                thumb=thumb_name,
                title=title,
                duration=dur,
                reply_markup=visit_butt,
            )
            if message.chat.type != ChatType.PRIVATE:
                await message.reply_text(
                    "ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘᴍ, sᴇɴᴛ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ sᴏɴɢ ᴛʜᴇʀᴇ."
                )
        except:
            start_butt = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ᴄʟɪᴄᴋ ʜᴇʀᴇ",
                            url=f"https://t.me/{BOT_USERNAME}?start",
                        )
                    ]
                ]
            )
            return await m.edit_text(
                text="ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴀɴᴅ sᴛᴀʀᴛ ᴍᴇ ғᴏʀ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ sᴏɴɢs.",
                reply_markup=start_butt,
            )
        await m.delete()
    except:
        return await m.edit_text("ғᴀɪʟᴇᴅ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴀᴜᴅɪᴏ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ sᴇʀᴠᴇʀs.")

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as ex:
        LOGGER.error(ex)
