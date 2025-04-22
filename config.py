import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
#BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "")

CHANNEL = os.environ.get("CHANNEL", "Anime_Lumino") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","V2_File_Renamer_bot") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","Anime_Chat_Group_V2") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","Anime_Lumino") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","I_am_Babi_villain")
STRING = os.environ.get("STRING", "BQGlhLEARnzKQUO9fhjjo65GWUVbf2OuowzqJYhqZDUclW029UEa4ix4Zl8ejr0pL8jdPkdCxPN8fgWzBxNSBniIGxfiqdvziRNweZ_PlI__1jsEVnD65pgLzdz8-ugPg8W5Fy5AGabAEzZ63AsLCIZk7DerIgcFx_NwEkjJ7y19eRYWybaHdFhVvPhjvVniCIRdVgI6Fc-dc9dztE2ZWRYWKjkb0wgPVRdgJwSRy5AtFmbHyeLfwsvRUkGUmES9jjVxzPZI2lxXu6D_-Rik0ryL0J02LvJoixGwYfXTcV3v3oh6S3jCEEdJtPDHKUsrLWDuRGZ7xcwrqNrIVt7ulkqauJE6FQAAAAGdpDQAAA")

DB_NAME = os.environ.get("DB_NAME","tirokaitube")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://tirokaitube:ymDe3VLWXQ05JazI@cluster0.tktl52k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "https://i.ibb.co/PvHsTVXC/x.jpg")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7823475125').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002568229104"))
