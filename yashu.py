from pyrogram import Client, filters, idle
from config import *
from EndUserbot.AlphaPlugins.sudo import *
from EndUserbot.AlphaPlugins.backup import *
from EndUserbot.AlphaPlugins.pmpermit import *
from EndUserbot.AlphaPlugins.block_unblock import *
from EndUserbot.AlphaPlugins.memify import *
from EndUserbot.AlphaPlugins.afk import *
from EndUserbot.AlphaPlugins.alive_or_ping import *
from EndUserbot.AlphaPlugins.stickers import kang
from EndUserbot.AlphaPlugins.lmao import lmao


pm_watcher = 1

USER = Client(":END-USERBOT:", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)


@USER.on_message(filters.command(["lmao", "lol"], COMMAND_HANDLER))
async def lmao_plug(_, m):
    await lmao(_, m)

@USER.on_message(filters.command(["alive", "ping", "end"], COMMAND_HANDLER))
async def alive_plug(_, m):
    await alive_or_ping(_, m)

@USER.on_message(filters.command("afk", COMMAND_HANDLER))
async def afk_plug(_, m):
    await set_afk(_, m)

@USER.on_message(group=2)
async def afk_cwf_plug(_, m):
    await afk_watcher(_, m)

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

@USER.on_message(filters.command(["kang", "steal"], COMMAND_HANDLER))
async def kang_plug(_, m):
    await kang(_, m)


USER.start()
get = USER.get_me()
OWNER = []
id = get.id
OWNER.append(id)
un = get.username
print(f"@{un} started successfully...!")
idle()
