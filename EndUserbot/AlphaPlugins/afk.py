from pyrogram import filters
from pyrogram.types import Message
from ..database import add_afk, remove_afk, is_afk, get_afk_details
import time 
from .utils import eor

async def set_afk(_, m):
    if not m.from_user.is_self:
        return
    if await is_afk(m.from_user.id):
        await remove_afk(m.from_user.id)
    try:
        afk_reason = m.text.split(None, 1)[1]
    except:
        afk_reason = "None"
    afk_time = time.time()
    details = {"afk_time": afk_time, "afk_reason": afk_reason}
    await add_afk(m.from_user.id, details)
    return await eor(m, f"<i>I shall be going AFK...</i>")

async def afk_watcher(_, m):
    l = await _.get_me()
    id = l.id
    unwa = l.username
    un = "@"+unwa
    afk = await is_afk(id)
    if not afk:
        return
    if m.from_user.is_self:
        try:
            if m.text.split()[0][1:].lower() == "afk":
                return
        except:
            pass
        DETAILS = await get_afk_details(m.from_user.id)
        await remove_afk(m.from_user.id)
        return_time = time.time()
        afk_time = DETAILS[0]
        afk_reason = DETAILS[1]
        time_afk = get_readable_time(int(retunr_time-afk_time))
        if afk_reason == "None":
            return await _.send_message(m.chat.id, f"<i>I'm back... into virtual world..!\n\nAway for {time_afk}</i>")
        return await _.send_message(m.chat.id, f"<i>I'm back... into virtual world..!\n\nAway for {time_afk}\n\nReason :- {afk_reason}</i>")
    else:
        reply = m.reply_to_message
        if (reply.from_user.id == id or un in m.text) and m.chat.type == "group":
            DETAILS = await get_afk_details(m.from_user.id)
            return_time = time.time()
            afk_time = DETAILS[0]
            afk_reason = DETAILS[1]
            time_afk = get_readable_time(int(retunr_time-afk_time))
            if afk_reason == "None":
                return await m.reply(f"<i>I'm AFK... \n\Since {time_afk}</i>")
            return await m.reply(f"<i>I'm AFK... \n\Since {time_afk}\n\nReason :- {afk_reason}</i>")
        elif m.chat.type == "private" and m.text:
            DETAILS = await get_afk_details(m.from_user.id)
            return_time = time.time()
            afk_time = DETAILS[0]
            afk_reason = DETAILS[1]
            time_afk = get_readable_time(int(retunr_time-afk_time))
            if afk_reason == "None":
                return await m.reply(f"<i>I'm AFK... \n\Since {time_afk}</i>")
            return await m.reply(f"<i>I'm AFK... \n\Since {time_afk}\n\nReason :- {afk_reason}</i>")
            
            

        
        
            
        
        
