import sys
import os
from pathlib import Path
import logging
from datetime import datetime
from pyrogram import Client
import sqlite3

# We need logging this early for our Version Check
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARN)
LOGS = logging.getLogger(__name__)

# Check for Python 3.6 or newer
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGS.error("You MUST use at least Python 3.6. Bot Quitting")
    quit(1)

# Now for the rest
__version__ = '0.0.1'
__author__ = 'Blondel MONDESIR'
__source__ = 'https://github.com/novaed/botserv'
__copyright__ = 'Copyright (c) 2019 ' + __author__
__copystring__ = f"BotServ v{__version__} | {__copyright__}"

# Change with genuine values
API_ID = 123456789
API_HASH = "dgsdfgsdfaa13232fsfw335"

LOGGER = True
try:
    LOGGER_GROUP = -12345567890
except ValueError:
    LOGGER_GROUP = "LOGGER_GROUP"

# Create Database if there is none yet.
BOTSERV_DB = str(Path(__file__).parent.parent / 'botserv.db')

LOGS.info("Checking Database...")
db = sqlite3.connect(BOTSERV_DB)
c = db.cursor()
c.executescript(
    "CREATE TABLE IF NOT EXISTS video_notes "
    "(name TEXT UNIQUE ON CONFLICT FAIL, file_id TEXT UNIQUE ON CONFLICT FAIL);"
    "CREATE TABLE IF NOT EXISTS welcome "
    "(chat_id INT UNIQUE ON CONFLICT FAIL, greet TEXT, chat_title TEXT);")
db.commit()
db.close()
LOGS.info("Check done.")


# Prepare the bot
BOT = Client(
    session_name="BotServ",
    api_id=API_ID,
    api_hash=API_HASH,
    app_version=f"BotServ \U0001f525\U0001F916 v{__version__}")

# Global Variables
ISAFK = False
AFK_REASON = "No Reason"
START_TIME = datetime.now()
