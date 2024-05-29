from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from Team-Legit-X-Music import BOT_USERNAME

pm_buttons = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text=" ᴄᴏᴍᴍᴀɴᴅs", callback_data="legit_help")],
    [
        InlineKeyboardButton(text=" ᴄʜᴀɴɴᴇʟ ", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text=" sᴜᴩᴩᴏʀᴛ ", url=config.SUPPORT_CHAT),
    ],
    [
        
        InlineKeyboardButton(text=" ᴅᴇᴠᴇʟᴏᴩᴇʀ ", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text=" ᴄʜᴀɴɴᴇʟ ", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text=" sᴜᴩᴩᴏʀᴛ ", url=config.SUPPORT_CHAT),
    ],
    [
      
        InlineKeyboardButton(text=" ᴅᴇᴠᴇʟᴏᴩᴇʀ ", user_id=config.OWNER_ID),
    ],
]
