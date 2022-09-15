from pyrogram import Client, filters, idle
from config import *
from EndUserbot.AlphaPlugins.sudo import *
from EndUserbot.AlphaPlugins.backup import *

USER = Client(":END-USERBOT:", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)

@USER.on_message(filters.command(["addsudo", "rmvsudo"], COMMAND_HANDLER))
async def sudo_plug(_, m):
    await add_or_del_sudo(_, m)

@USER.on_message(filters.command("sudos", COMMAND_HANDLER))
async def get_sudos_plug(_, m):
    await sudo_users(_, m)

@USER.on_message(filters.command("backup", COMMAND_HANDLER))
async def backup_plug(_, m):
    await backup(_, m)

USER.start()
get = USER.get_me()
OWNER = []
id = get.id
OWNER.append(id)
un = get.username
print(f"@{un} started successfully...!")
idle()
