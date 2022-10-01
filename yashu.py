from pyrogram import Client, filters, idle
from config import *
from EndUserbot.AlphaPlugins.sudo import *
from EndUserbot.AlphaPlugins.backup import *
from EndUserbot.AlphaPlugins.pmpermit import *
from EndUserbot.AlphaPlugins.block_unblock import *
from EndUserbot.AlphaPlugins.memify import *

pm_watcher = 1

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

@USER.on_message(filters.command("setlog", COMMAND_HANDLER))
async def setlog_plug(_, m):
    await set_log(_, m)

@USER.on_message(filters.command("pmpermit", COMMAND_HANDLER))
async def pm_permit_plug(_, m):
    await pm_protect(_, m)

@USER.on_message(filters.command(["a", "approve", "allow", "da", "disapprove", "disallow"], COMMAND_HANDLER))
async def approve_disapprove_plug(_, m):
    await approve_disapprove(_, m)

@USER.on_message(group=pm_watcher)
async def pm_watcher_plug(_, m):
    await pm_cwf(_, m)

@USER.on_message(filters.command(["block", "unblock"], COMMAND_HANDLER))
async def block_unblock_plug(_, m):
    await block_or_unblock_user(_, m)

@USER.on_message(filters.command(["mmf", "memify"], COMMAND_HANDLER))
async def memify_plug(_, m):
    await memify_event(_, m)


USER.start()
get = USER.get_me()
OWNER = []
id = get.id
OWNER.append(id)
un = get.username
print(f"@{un} started successfully...!")
idle()
