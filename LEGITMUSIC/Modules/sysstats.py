import platform
import re
import socket
import uuid
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls.__version__ import __version__ as pytgver

from LEGITMUSIC import BOT_NAME, SUDOERS, app
from LEGITMUSIC.Modules import ALL_MODULES


@app.on_message(filters.command(["stats", "sysstats"]) & SUDOERS)
async def sys_stats(_, message: Message):
    sysrep = await message.reply_text(
        f"ɢᴇᴛᴛɪɴɢ {BOT_NAME} sʏsᴛᴇᴍ sᴛᴀᴛs, ɪᴛ'ʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ..."
    )
    try:
        await message.delete()
    except:
        pass
    sudoers = len(SUDOERS)
    mod = len(ALL_MODULES)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    architecture = platform.machine()
    processor = platform.processor()
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    sp = platform.system()
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " ɢʙ"
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}ɢʜᴢ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}ᴍʜᴢ"
    except:
        cpu_freq = "ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    platform_release = platform.release()
    platform_version = platform.version()

    await sysrep.edit_text(
        f"""
➻ <u>**{BOT_NAME} sʏsᴛᴇᴍ sᴛᴀᴛs**</u>

**ᴩʏᴛʜᴏɴ :** {pyver.split()[0]}
**ᴩʏʀᴏɢʀᴀᴍ :** {pyrover}
**ᴩʏ-ᴛɢᴄᴀʟʟs :** {pytgver}
**sᴜᴅᴏᴇʀs :** `{sudoers}`
**ᴍᴏᴅᴜʟᴇs :** `{mod}`

**ɪᴘ :** {ip_address}
**ᴍᴀᴄ :** {mac_address}
**ʜᴏsᴛɴᴀᴍᴇ :** {hostname}
**ᴘʟᴀᴛғᴏʀᴍ :** {sp}
**ᴘʀᴏᴄᴇssᴏʀ :** {processor}
**ᴀʀᴄʜɪᴛᴇᴄᴛᴜʀᴇ :** {architecture}
**ᴘʟᴀᴛғᴏʀᴍ ʀᴇʟᴇᴀsᴇ :** {platform_release}
**ᴘʟᴀᴛғᴏʀᴍ ᴠᴇʀsɪᴏɴ :** {platform_version}

        <b><u>sᴛᴏʀᴀɢᴇ</b><u/>
**ᴀᴠᴀɪʟᴀʙʟᴇ :** {total[:4]} ɢɪʙ
**ᴜsᴇᴅ :** {used[:4]} ɢɪʙ
**ғʀᴇᴇ :** {free[:4]} ɢɪʙ

**ʀᴀᴍ :** {ram}
**ᴩʜʏsɪᴄᴀʟ ᴄᴏʀᴇs :** {p_core}
**ᴛᴏᴛᴀʟ ᴄᴏʀᴇs :** {t_core}
**ᴄᴩᴜ ғʀᴇǫᴜᴇɴᴄʏ :** {cpu_freq}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ᴄʟᴏsᴇ",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        ),
    )
