from ..database.afk import *
from importer import OWNER
from pyrogram.types import Message
from pyrogram import Client
import time
from .utils import eor, get_me

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

async def _afk(_: Client, m: Message):
    if not m.from_user.id in OWNER:
        return
    if await is_afk(m.from_user.id):
        await del_afk(m.from_user.id)
        if len(m.command) > 1:
            reason = m.text.split(None, 1)[1]
        else:
            reason = "None"
        __time = time.time()
        try:
            await add_afk(m.from_user.id, reason, str(__time))
            if not reason == "None":
                return await eor(m, f"`I shall be Going afk! because ~` {reason}")
            else:
                return await eor(m, f"`I shall be Going afk!")
        except Exception as e:
            return await eor(m, e)


    else:
        if len(m.command) > 1:
            reason = m.text.split(None, 1)[1]
        else:
            reason = "None"
        __time = time.time()
        try:
            await add_afk(m.from_user.id, reason, str(__time))
            if not reason == "None":
                return await eor(m, f"`I shall be Going afk! because ~` {reason}")
            else:
                return await eor(m, f"`I shall be Going afk!")
        except Exception as e:
            return await eor(m, e)

async def afk_cwf(_, m):
    if m.from_user.id in OWNER and not m.text.split()[0][1:4].lower() == "afk":
        check = await is_afk(m.from_user.id)
        if not check:
            return
        reason, time_st = await get_afk_details(m.from_user.id)
        await del_afk(m.from_user.id)
        time_end = time.time()
        afk_for = get_readable_time(int(time_end - float(time_st))) + "s"
        return await _.send_message(m.chat.id, 
            "`Back alive! No Longer afk.\nWas afk for " + afk_for + "`"
        )
    
    if not m.from_user.id in OWNER and m.chat.type == "group":
        if not m.reply_to_message:
            xD = await get_me(_)
            un = "@"+xD.username.lower()
            if not un in m.text.split().lower():
                return
            check = await is_afk(xD.id)
            if not check:
                return
            reason, _time = await get_afk_details(xD.id)
            afk_for = get_readable_time(int(time.time()-float(_time))) + "s"
            if not reason == "None":
                return await m.reply(f"`I am AFK .\n\nAFK Since {afk_for}\nReason : {reason}`")
            return await m.reply(f"`I am AFK .\n\nAFK Since {afk_for}`")
            
        check = await is_afk(m.reply_to_message.from_user.id)
        if not check:
            return
        reason, _time = await get_afk_details(m.reply_to_message.from_user.id)
        afk_for = get_readable_time(int(time.time()-float(_time))) + "s"
        if not reason == "None":
            return await m.reply(f"`I am AFK .\n\nAFK Since {afk_for}\nReason : {reason}`")
        return await m.reply(f"`I am AFK .\n\nAFK Since {afk_for}`")

    if not m.from_user.id in OWNER and m.chat.type == "private":
        xD = await get_me(_)
        check = await is_afk(xD.id)
        if not check:
            return
        reason, _time = await get_afk_details(m.reply_to_message.from_user.id)
        afk_for = get_readable_time(int(time.time()-float(_time))) + "s"
        if not reason == "None":
            return await m.reply(f"`I am AFK .\n\nAFK Since {afk_for}\nReason : {reason}`")
        return await m.reply(f"`I am AFK .\n\nAFK Since {afk_for}`")

        
    
    
