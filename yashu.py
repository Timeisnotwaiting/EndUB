from pyrogram import Client, filters, idle
from config import *
from EndUserbot.AlphaPlugins import *

USER = Client(":END-USERBOT:", API_ID, API_HASH, STRING_SESSION)

@USER.on_message(filters.command("afk", COMMAND_HANDLER))
async def afk(_, m):
    await _afk(_, m)

@USER.on_message(group=1)
async def __afk(_, m):
    await afk_cwf(_, m)

USER.start()
get = USER.get_me()
un = get.username
print(f"@{un} started successfully...!")
idle()
