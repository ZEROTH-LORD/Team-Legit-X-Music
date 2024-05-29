from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", "7186198304:AAH411vuq4UzwJroUeXR9Uv1DMYFkwtACwU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "7453770651"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/f490a906797896349632c.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/f490a906797896349632c.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Team_Legit_X")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Team_Legit_X")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7453770651").split()))


