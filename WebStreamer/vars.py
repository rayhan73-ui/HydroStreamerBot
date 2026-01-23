# This file is a part of FileStreamBot
from urllib import request
from os import environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(environ.get("API_ID"))
    API_HASH = str(environ.get("API_HASH"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN"))
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))
    WORKERS = int(environ.get("WORKERS", "6"))
    BIN_CHANNEL = int(environ.get("BIN_CHANNEL"))
    
    # Render এর জন্য পোর্ট ম্যানেজমেন্ট
    PORT = int(environ.get("PORT", 8080))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
    
    # Render এবং HTTPS এর জন্য ফিক্সড লজিক
    HAS_SSL = str(environ.get("HAS_SSL", "True").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(environ.get("NO_PORT", "True").lower()) in ("1", "true", "t", "yes", "y")
    
    # FQDN থেকে প্রোটোকল সরিয়ে ক্লিন ডোমেইন নেওয়া
    FQDN = str(environ.get("FQDN", BIND_ADDRESS)).replace("https://", "").replace("http://", "").strip("/")
    
    # URL তৈরি: Render ডোমেইন হলে সরাসরি HTTPS ব্যবহার করবে
    if "onrender.com" in FQDN:
        URL = f"https://{FQDN}/"
    else:
        URL = "http{}://{}{}/".format(
            "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
        )

    DATABASE_URL = str(environ.get('DATABASE_URL'))
    UPDATES_CHANNEL = str(environ.get('UPDATES_CHANNEL', "Telegram"))
    OWNER_ID = int(environ.get('OWNER_ID'))
    SESSION_NAME = str(environ.get('SESSION_NAME', 'hydroBot'))
    
    FORCE_UPDATES_CHANNEL = environ.get('FORCE_UPDATES_CHANNEL', "False")
    FORCE_UPDATES_CHANNEL = True if str(FORCE_UPDATES_CHANNEL).lower() == "true" else False
    
    ALLOWED_USERS = [x.strip("@ ") for x in str(environ.get("ALLOWED_USERS") or "").split(",") if x.strip("@ ")]

    # KEEP_ALIVE এবং অন্যান্য ডিফল্ট
    KEEP_ALIVE = str(environ.get("KEEP_ALIVE", "1").lower()) in ("1", "true", "t", "yes", "y")
    IMAGE_FILEID = environ.get('IMAGE_FILEID', "https://cdn.jsdelivr.net/gh/fyaz05/Resources@main/HydroStreamerBot/My%20Files.jpeg")
    
    TOS = environ.get("TOS", None)
    if TOS:
        try:
            response = request.urlopen(TOS)
            data = response.read().decode('utf-8')
            TOS = data.strip()
        except:
            TOS = None

    MODE = environ.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    LINK_LIMIT = int(environ.get("LINK_LIMIT")) if "LINK_LIMIT" in environ else None
