from pyrogram import Client, filters, idle
from config import *


USER = Client(":END-USERBOT:", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)



USER.start()
get = USER.get_me()
OWNER = []
id = get.id
OWNER.append(id)
un = get.username
print(f"@{un} started successfully...!")
idle()
