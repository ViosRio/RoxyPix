import os

# Temel Bot Ayarları
API_ID = int(os.environ.get("API_ID", "20658336"))
API_HASH = os.environ.get("API_HASH", "cedfb5fb4ffee7ecc746b28afc7925e3") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
BOT_USERNAME = os.environ.get("BOT_USERNAME", "LunaGramBot") 
SUDO_USERS = list(map(int, os.environ.get("SUDO", "5910057231").split()))  # Çoklu sudo desteği
BOT_NAME = os.environ.get("BOT_NAME", "THENA")

# Bot Görselleri
START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/4746e2442a584f37dcc86.jpg")
STKR = os.environ.get("STKR", "CAACAgEAAx0CRjAUHgABAsULZASkFZUsTQTw2k-FvC2SBJnd-vAAAokCAALW9iBFzemsQBDIqWkuBA")

# Limitler
MAX_FILE_SIZE = int(os.environ.get("MAX_FILE_SIZE", 20242880))  # 20 MB
ALLOWED_EXTENSIONS = os.environ.get("ALLOWED_EXTENSIONS", "jpg,png,sql,csv,mp4").split(",")

# Sosyal Bağlantılar
UPDATE_CHNL = os.environ.get("UPDATE_CHNL", "ViosTeam")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP", "Bot4Chan")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "ViosCeo")

# Güvenlik
BANNED_USERS = list(map(int, os.environ.get("BANNED_USERS", "").split())) if os.environ.get("BANNED_USERS") else []
