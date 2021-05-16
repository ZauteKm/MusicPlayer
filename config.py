
import os
import re


class Config:
    ADMIN = os.environ.get("ADMINS", '')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", 111111))
    CHAT = int(os.environ.get("CHAT", ""))
    LOG_GROUP=os.environ.get("LOG_GROUP", "")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=os.environ.get("STREAM_URL", "https://eu10.fastcast4u.com/clubfmuae")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    SESSION = os.environ.get("SESSION_STRING", "")

