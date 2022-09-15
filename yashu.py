from pyrogram import Client, filters, idle
from config import *
from EndUserbot.AlphaPlugins.afk import _afk, afk_cwf

USER = Client(":END-USERBOT:", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)

@USER.on_message(filters.command("afk", COMMAND_HANDLER))
async def afk(_, m):
    await _afk(_, m)

@USER.on_message(group=1)
async def __afk(_, m):
    await afk_cwf(_, m)

USER.start()
get = USER.get_me()
OWNER = []
id = get.id
OWNER.append(id)
un = get.username
print(f"@{un} started successfully...!")
idle()
