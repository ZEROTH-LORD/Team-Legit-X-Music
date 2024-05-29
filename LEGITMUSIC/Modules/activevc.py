from pyrogram import filters
from pyrogram.types import Message

from LEGITMUSIC import SUDOERS, app
from LEGITMUSIC.help.active import get_active_chats
from LEGITMUSIC.help.inline import close_key


@app.on_message(filters.command("activevc") & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs ʟɪsᴛ...")
    chats = await get_active_chats()
    text = ""
    j = 0
    for chat in chats:
        try:
            title = (await app.get_chat(chat)).title
        except Exception:
            title = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        if (await app.get_chat(chat)).username:
            user = (await app.get_chat(chat)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{chat}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs ᴏɴ ᴍᴜsɪᴄʙᴏᴛ...")
    else:
        await mystic.edit_text(
            f"**ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs ᴏɴ ᴍᴜsɪᴄ ʙᴏᴛ :**\n\n{text}",
            reply_markup=close_key,
            disable_web_page_preview=True,
        )
