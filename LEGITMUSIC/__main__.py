import asyncio
import importlib
import os

from pyrogram import idle

from LEGITMUSIC import (
    ASS_ID,
    ASS_NAME,
    ASS_USERNAME,
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    SUNAME,
    app,
    app2,
    pytgcalls,
)
from LEGITMUSIC.Modules import ALL_MODULES


async def legit_startup():
    LOGGER.info("[•] Loading Modules...")
    for module in ALL_MODULES:
        importlib.import_module("LEGITMUSIC.Modules." + module)
    LOGGER.info(f"[•] Loaded {len(ALL_MODULES)} Modules.")

    LOGGER.info("[•] Refreshing Directories...")
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")
    LOGGER.info("[•] Directories Refreshed.")

    try:
        await app.send_message(
            SUNAME,
            f"✯ Legit ᴍᴜsɪᴄ ʙᴏᴛ ✯\n\n𖢵 ɪᴅ : `{BOT_ID}`\n𖢵 ɴᴀᴍᴇ : {BOT_NAME}\n𖢵 ᴜsᴇʀɴᴀᴍᴇ : @{BOT_USERNAME}",
        )
    except Exception as e:
        LOGGER.error(
            f"{BOT_NAME} failed to send message at @{SUNAME}, please go & check. Error: {e}"
        )

    try:
        await app2.send_message(
            SUNAME,
            f"✯ Legit ᴍᴜsɪᴄ ᴀss ✯\n\n𖢵 ɪᴅ : `{ASS_ID}`\n𖢵 ɴᴀᴍᴇ : {ASS_NAME}\n𖢵 ᴜsᴇʀɴᴀᴍᴇ : @{ASS_USERNAME}",
        )
    except Exception as e:
        LOGGER.error(
            f"{ASS_NAME} failed to send message at @{SUNAME}, please go & check. Error: {e}"
        )

    await app2.send_message(BOT_USERNAME, "/start")

    LOGGER.info(f"[•] Bot Started As {BOT_NAME}.")
    LOGGER.info(f"[•] Assistant Started As {ASS_NAME}.")

    LOGGER.info(
        "[•] \x53\x74\x61\x72\x74\x69\x6e\x67\x20\x50\x79\x54\x67\x43\x61\x6c\x6c\x73\x20\x43\x6c\x69\x65\x6e\x74\x2e\x2e\x2e"
    )
    await pytgcalls.start()
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(legit_startup())
    LOGGER.error("legit Music Bot Stopped.")
