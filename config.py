import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
OWNER_NAME = getenv("OWNER_NAME", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
ALIVE_NAME = getenv("ALIVE_NAME", "")
BOT_USERNAME = getenv("BOT_USERNAME")
OWNER_ID = getenv("OWNER_ID")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/8e8e9b412e2eab6789ecd.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d762a907265ab2ab1950e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Noobxcoders/BLINK-MUSICS")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/8e8e9b412e2eab6789ecd.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/d762a907265ab2ab1950e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/06759aac4cf965ff27dce.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/41e4113d6fb2dc8a3c39b.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/8ac73da2a18aef2db211d.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/823eb7c0ef4e1af3bc94a.jpg")
