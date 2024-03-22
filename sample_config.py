# PLEASE STOP!
# DO NOT EDIT THIS FILE OR DELETE THIS FILE
# Create a new config.py file in same directory and import, then extend this class.

import os
from typing import Set

from telethon.tl.types import ChatBannedRights
from validators.url import url


class Config(object):
    LOGGER = True
    # MUST NEEDED VARS
    PORT = os.environ.get("PORT", None)
    # set this value with your name
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    # Get the values for following 2 from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH") or None
    # Datbase url heroku sets it automatically else get this from elephantsql
    DB_URI = os.environ.get("DATABASE_URL", None)
    # Get this value by running python3 stringsetup.py or https://repl.it/@zedthonn/stringsession
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    # Telegram BOT Token and bot username from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN") or os.environ.get(
        "TG_BOT_TOKEN_BF_HER", None
    )
    TG_BOT_USERNAME = None
    # get this value from http://www.timezoneconverter.com/cgi-bin/findzone.tzc
    TZ = os.environ.get("TZ", "Asia/Baghdad")
    # set this with required zed repo link
    UPSTREAM_REPO = os.environ.get(
        "UPSTREAM_REPO", "https://github.com/Telegram-R2RR7/SourceM"
    )
    # External plugins repo
    EXTERNAL_REPO = os.environ.get("EXTERNAL_REPO", None)
    VCMODE = os.environ.get("VCMODE", False)
    VCMODE = bool(VCMODE and (VCMODE.lower() != "false"))
    VC_SESSION = os.environ.get("VC_SESSION", None)
    # if you need badcat plugins use the following vars
    OLDZED = os.environ.get("OLDZED", "no")
    OLDZED = bool(OLDZED and (OLDZED.lower() != "no"))
    # BASIC and MAIN CONFIG VARS
    # for profile default name
    # Set this value with group id of private group(can be found this value by .id)
    PRIVATE_GROUP_BOT_API_ID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID") or 0)
    # Set this value same as PRIVATE_GROUP_BOT_API_ID if you need pmgaurd
    PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID") or 0)
    # Set this value for working of fban/unfban/superfban/superunfban cmd
    FBAN_GROUP_ID = int(os.environ.get("FBAN_GROUP_ID") or 0)
    # set this value with channel id of private channel use full for .frwd cmd
    PRIVATE_CHANNEL_BOT_API_ID = int(os.environ.get("PRIVATE_CHANNEL_BOT_API_ID") or 0)
    # for heroku plugin you can get this value from https://dashboard.heroku.com/account
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    # set this with same app name you given for heroku
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    # Owner id to show profile link of given id as owner
    OWNER_ID = int(os.environ.get("OWNER_ID") or 0)
    # رسائل تحذيرات الحماية
    MAX_FLOOD_IN_PMS = int(os.environ.get("MAX_FLOOD_IN_PMS", 6))
    # set this with group id so it keeps notifying about your tagged messages or pms
    PM_LOGGER_GROUP_ID = int(
        os.environ.get("PM_LOGGER_GROUP_ID")
        or os.environ.get("PM_LOGGR_BOT_API_ID")
        or 0
    )

    #فارات زدثــون
    CUSTOM_ALIVE_TEXT = os.environ.get("CUSTOM_ALIVE_TEXT", None)
    CUSTOM_ALIVE_EMOJI = os.environ.get("CUSTOM_ALIVE_EMOJI", None)
    CUSTOM_ALIVE_EMZED = os.environ.get("CUSTOM_ALIVE_EMZED", None)
    CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
    ZELZAL_Z = int(1338009605)
    ZELZAL_A = int(os.environ.get("ZELZAL_A") or -1001338009605)
    ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
    BOT_PIC = os.environ.get("BOT_PIC", None)
    ZED_MEDIA = os.environ.get("ZED_MEDIA", None)
    BOT_HANDLER = os.environ.get("BOT_HANDLER", "^;")
    PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
    DIGITAL_PIC = os.environ.get("DIGITAL_PIC", None)
    DEFAULT_PIC = os.environ.get("DEFAULT_PIC", None)
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
    DEFAULT_NAME = os.environ.get("DEFAULT_NAME", None)
    ZI_FN = os.environ.get("ZI_FN", "𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬")
    CUSTOM_PMPERMIT_TEXT = os.environ.get("CUSTOM_PMPERMIT_TEXT", None)

    # Custom vars for zthon
    # set this will channel id of your custom plugins
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL") or 0)
    # set this value with your required name for telegraph plugin
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "ZThon")
    # for custom thumb image set this with your required thumb telegraoh link
    THUMB_IMAGE = os.environ.get(
        "THUMB_IMAGE", "https://telegra.ph/file/ee6ce6991f3ca199517bf.jpg"
    )
    # specify NO_LOAD with plugin names for not loading in userbot
    NO_LOAD = list(os.environ.get("NO_LOAD", "").split())
    # specify command handler that should be used for the plugins
    # this should be a valid "regex" pattern
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r".")
    SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r".")
    # set this with required folder path to act as download folder
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "downloads")
    # set this with required folder path to act as temparary folder
    TEMP_DIR = os.environ.get("TEMP_DIR", "./temp/")
    # SpamWatch, CAS, SpamProtection ban Needed or not
    ANTISPAMBOT_BAN = os.environ.get("ANTISPAMBOT_BAN", False)
    # progress bar progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "▰")
    UNFINISHED_PROGRESS_STR = os.environ.get("UNFINISHED_PROGRESS_STR", "▱")

    # API VARS FOR ZTHON
    # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture for screen shot
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
    # Get your own APPID from https://api.openweathermap.org/data/2.5/weather
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    # This is required for the speech to text plugin. Get your USERNAME from
    # https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    # Get free api from https://dashboard.ipdata.co/sign-up.html
    IPDATA_API = os.environ.get("IPDATA_API", None)
    # Get a Free API Key from OCR.Space
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    # Genius lyrics get this value from https://genius.com/developers both has
    GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None)
    # Get your own API key from https://www.remove.bg/
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    # Get this value from https://free.currencyconverterapi.com/
    CURRENCY_API = os.environ.get("CURRENCY_API", None)
    # Google Drive plugin https://telegra.ph/G-Drive-guide-for-catuserbot-01-01
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
    G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
    G_DRIVE_INDEX_LINK = os.environ.get("G_DRIVE_INDEX_LINK", None)
    # For transfer channel 2 step verification code of telegram
    TG_2STEP_VERIFICATION_CODE = os.environ.get("TG_2STEP_VERIFICATION_CODE", None)
    # JustWatch Country for watch plugin
    WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "IN")
    # Last.fm plugin  https://telegra.ph/Guide-for-LASTFM-02-03
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    # Spotify API for spotify.py // get from here :  https://developer.spotify.com/dashboard/login
    SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID", None)
    SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET", None)
    # SpamWatch API you can get it from get api from http://t.me/SpamWatchBot?start=token
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    # can get from https://coffeehouse.intellivoid.net/
    RANDOM_STUFF_API_KEY = os.environ.get("RANDOM_STUFF_API_KEY", None)
    # github vars
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Deepai value can get from https://deepai.org/
    DEEP_AI = os.environ.get("DEEP_AI", None)

    # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
    # TG API limit. A message can have maximum 4096 characters!
    MAX_MESSAGE_SIZE_LIMIT = 4095
    # specify LOAD and NO_LOAD
    LOAD = []
    # warn mode for anti flood
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None, view_messages=None, send_messages=True
    )
    CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    CHROME_DRIVER = os.environ.get(
        "CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver"
    )
    # for sed plugin
    GROUP_REG_SED_EX_BOT_S = os.environ.get(
        "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
    )
    # time.py
    COUNTRY = str(os.environ.get("COUNTRY", ""))
    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
    # For updater plugin
    UPSTREAM_REPO_BRANCH = os.environ.get("UPSTREAM_REPO_BRANCH", "lite")
    # dont touch this at all
    SUDO_USERS: Set[int] = set()
    ZEDUBLOGO = None
    BOTLOG = False
    BOTLOG_CHATID = 0
    # extra plugins realted vars below  4
    EXTERNAL_REPOBRANCH = os.environ.get("EXTERNAL_REPOBRANCH", "main")
    OLDZED_REPO = os.environ.get("OLDZED_REPO", "https://github.com/Zed-Thon/ZED_USERBOT")
    if OLDZED_REPO and not url(OLDZED_REPO):
        OLDZED_REPO = "https://github.com/Zed-Thon/ZED_USERBOT"
    OLDZED_REPOBRANCH = os.environ.get("OLDZED_REPOBRANCH", "oldzed")
    VC_REPO = os.environ.get("VC_REPO", "https://github.com/Zed-Thon/ZVCPlayer")
    VC_REPOBRANCH = os.environ.get("VC_REPOBRANCH", "zvcplayer")

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
