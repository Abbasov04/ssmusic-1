import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "26559392"))
API_HASH = getenv("API_HASH", "f4b51bbe7b22ba48170024f8f82d04d5")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6370639090:AAFw1NaE3IgSg2aOzXgjiuyGvRqS3djNHho")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://nicatovnicat17:<password>@cluster0.xkr5yix.mongodb.net/")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's antivirus 
LOGGER_ID = int(getenv("LOGGER_ID", "-1002234078391"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6585468162"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Nicat42/ssmusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/yoxlamaqsupport")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/yoxlamaqsupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", False)
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "AgF5ac4AaRXp6etnCfDqMopWcvD9ZRCa9k4JVRM0RggytFAMP3uT9mKib5hos15BmuFSRtwgubFpnCgHR-Rig7NG4jj33Wvsmsw-ugSupWqMv2guy-7licwpoG0alSnE4BjpmH-TjyigdkEBvSawVxdJj-43p3tIfPwB0810SKkiBK-EuLDG422Whkm7SIqheg7HDLGQl3OMxO6mzzkQAOPS8OUl4KlSN2uHWNQGoZfNXCL5CBH7UQqLU4un8lTGfmOCnvuw5SqDOU2dTj6btPFgWgJfJQwJbkkK7pJVEd026K4639bqCy74FfozZGwaK1m2nPdKOdValaRGrIbFBlCoq3gZAAAAAAGlQQYVAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/90d5dbb28269820702283.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/90d5dbb28269820702283.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
STATS_IMG_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
