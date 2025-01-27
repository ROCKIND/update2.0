import re
import os
from os import environ
from Script import script
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '27924747'))
API_HASH = environ.get('API_HASH', 'ce0f307805e68df9a18e1eac53048610')
BOT_TOKEN = environ.get('BOT_TOKEN', '6584350581:AAHNPWxgIEXhkLMtv1ayigN1gFsFDpycePc')

PICS = (environ.get('PICS', 'https://telegra.ph/file/f515fbc2084592eca60a5.jpg https://telegra.ph/file/f0aa4f433132769f8970c.jpg https://telegra.ph/file/58fef5cb458d5b29b0186.jpg https://telegra.ph/file/6045ba953af4def846238.jpg https://telegra.ph/file/20dbdcffaa89bd3d09a74.jpg https://telegra.ph/file/f515fbc2084592eca60a5.jpg')).split() #SAMPLE PIC
START_IMG = environ.get('START_IMG', 'https://telegra.ph/file/f515fbc2084592eca60a5.jpg')
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/d7c9c7906833797aa0244.jpg')
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1393092521 6300461900').split()]
USERNAME = environ.get('USERNAME', "https://telegram.me/Your_raj")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001651812610'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/SB_Movie_Group')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001917260095').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://raj94626:sona779988@cluster0.puujdfx.mongodb.net/?retryWrites=true&w=majority")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @Sb_Botz_Update</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

#chatgptAI
AI = is_enabled((environ.get("AI","True")), True)
OPENAI_API = environ.get("OPENAI_API", "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")
DEEP_API = environ.get("DEEP_API", "3ac9b077-654f-45c6-a1f0-a04a5ef6b69e")
GOOGLE_API_KEY = environ.get("GOOGLE_API_KEY", "AIzaSyDAiofJYzPZD1p_qty6S76rrNkcTB812mY")
AI_LOGS = int(environ.get("AI_LOGS", "-1001963473990")) #GIVE YOUR NEW LOG CHANNEL ID TO STORE MESSAGES THAT THEY SEARCH IN BOT PM.... [ i have added this to keep an eye on the users message, to avoid misuse of Bot ]

DATABASE_NAME = environ.get('DATABASE_NAME', "cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1001963473990'))
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','-1001764238165'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1001764238165'))
URL = environ.get('URL', 'sb-file-stream-598aab65b298.herokuapp.com') # your deployment url
STICKERS_IDS = ('CAACAgUAAxkBAAEC5s1mfmbnUx4f7jYODXqmoDo_QltzLQACmw4AAl3VAVYieASlHlskATUE').split()
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1001963473990'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/SB_Botz_Update/104")
SHORTENER_API = environ.get("SHORTENER_API", "651a3be83904f861a882e9417c6e25f857857802")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'omegalinks.in')
SHORTENER_API2 = environ.get("SHORTENER_API2", "651a3be83904f861a882e9417c6e25f857857802")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'omegalinks.in')
SHORTENER_API3 = environ.get("SHORTENER_API3", "651a3be83904f861a882e9417c6e25f857857802")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'omegalinks.in')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))

LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
auth_channel = environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1001625752177'))
request_channel = environ.get('REQUEST_CHANNEL', '-1001838363129')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
UPI_PAY_LOGS = int(environ.get('UPI_PAY_LOGS', '-1001963473990'))
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002176919909'))
IGNORE_WORDS = (list(os.environ.get("IGNORE_WORDS").split(",")) if os.environ.get("IGNORE_WORDS") else [])
IGNORE_WORDS=["movies", "Movies", ",", "episode", "Episode", "episodes", "Episodes", "south indian", "south indian movie", "South Indian Movie", "south movie", "South Movie", "South Indian", "web-series", "punjabi", "marathi", "hindi me bhejo", "hindi", "gujrati", "combined", "!", "kro", "jaldi", "Audio", "audio", "movi", "language", "Language", "Hollywood", "All", "all", "bollywood", "Bollywood", "South", "south", "HD", "hd", "karo", "Karo", "fullepisode", "please", "plz", "Please", "Plz", "send", "link", "Link", "full", "Full", "dabbed", "dubbed", "gujarati", "gujrati", "Gujarati", "Gujrati", "season", "Season", "web", "series", "Web", "Series", "webseries", "WebSeries", "upload", "HD", "Hd", "bhejo", "ful", "Send", "Bhejo", "movie"]
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 300))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
    }
DEFAULT_POST_MODE = {
    'singel_post_mode' : True,
    'all_files_post_mode' : True
}
