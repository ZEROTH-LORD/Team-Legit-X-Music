from pyrogram import filters
from pyrogram.types import Message

from LEGITMUSIC import ASS_MENTION, LOGGER, SUDOERS, app, app2


@app.on_message(filters.command(["asspfp", "setpfp"]) & SUDOERS)
async def set_pfp(_, message: Message):
    if message.reply_to_message.photo:
        fuk = await message.reply_text("» ᴄʜᴀɴɢɪɴɢ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ...")
        img = await message.reply_to_message.download()
        try:
            await app2.set_profile_photo(photo=img)
            return await fuk.edit_text(
                f"» {ASS_MENTION} ᴘʀᴏғɪʟᴇ ᴘɪᴄ ᴄʜᴀɴɢᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ."
            )
        except:
            return await fuk.edit_text("» ғᴀɪʟᴇᴅ ᴛᴏ ᴄʜᴀɴɢᴇ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ.")
    else:
        await message.reply_text(
            "» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ғᴏʀ ᴄʜᴀɴɢɪɴɢ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ."
        )


@app.on_message(filters.command(["delpfp", "delasspfp"]) & SUDOERS)
async def set_pfp(_, message: Message):
    try:
        pfp = [p async for p in app2.get_chat_photos("me")]
        await app2.delete_profile_photos(pfp[0].file_id)
        return await message.reply_text(
            "» sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ."
        )
    except Exception as ex:
        LOGGER.error(ex)
        await message.reply_text("» ғᴀɪʟᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ.")


@app.on_message(filters.command(["assbio", "setbio"]) & SUDOERS)
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            await app2.update_profile(bio=newbio)
            return await message.reply_text(
                f"» {ASS_MENTION} ʙɪᴏ ᴄʜᴀɴɢᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ."
            )
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        await app2.update_profile(bio=newbio)
        return await message.reply_text(f"» {ASS_MENTION} ʙɪᴏ ᴄʜᴀɴɢᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.")
    else:
        return await message.reply_text(
            "» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ɪᴛ ᴀs ᴀssɪsᴛᴀɴᴛ's ʙɪᴏ."
        )


@app.on_message(filters.command(["assname", "setname"]) & SUDOERS)
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            await app2.update_profile(first_name=name)
            return await message.reply_text(
                f"» {ASS_MENTION} ɴᴀᴍᴇ ᴄʜᴀɴɢᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ."
            )
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        await app2.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"» {ASS_MENTION} ɴᴀᴍᴇ ᴄʜᴀɴɢᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.")
    else:
        return await message.reply_text(
            "» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ɪᴛ ᴀs ᴀssɪsᴛᴀɴᴛ's ɴᴇᴡ ɴᴀᴍᴇ."
        )
