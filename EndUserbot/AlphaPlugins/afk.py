from pyrogram import filters
from pyrogram.types import Message
from ..database import add_afk, remove_afk, is_afk, get_afk_details
import time 
from .utils import eor

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

USER = []
async def afk_watcher(_, m):
    global USER
    if not USER:
        l = await _.get_me()
        id = l.id
        unwa = l.username
        un = "@"+unwa
        USER.append(id)
        USER.append(un)
    id = USER[0]
    un = USER[1]
    afk = await is_afk(id)
    if not afk:
        return
    if m.from_user.id == id:
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
        time_afk = get_readable_time(int(return_time-afk_time))
        if afk_reason == "None":
            return await _.send_message(m.chat.id, f"<i>I'm back... into virtual world..!\n\nAway for {time_afk}</i>")
        return await _.send_message(m.chat.id, f"<i>I'm back... into virtual world..!\n\nAway for {time_afk}\n\nReason :- {afk_reason}</i>")
    else:
        if str(m.chat.id)[0] != "-":
            DETAILS = await get_afk_details(id)
            return_time = time.time()
            afk_time = DETAILS[0]
            afk_reason = DETAILS[1]
            time_afk = get_readable_time(int(return_time-afk_time))
            if afk_reason == "None":
                return await m.reply(f"<i>I'm AFK... \n\nSince {time_afk}</i>")
            return await m.reply(f"<i>I'm AFK... \n\nSince {time_afk}\n\nReason :- {afk_reason}</i>")
        elif str(m.chat.id)[0] == "-":
            if m.reply_to_message:
                if m.reply_to_message.from_user.id == id:
                    DETAILS = await get_afk_details(id)
                    return_time = time.time()
                    afk_time = DETAILS[0]
                    afk_reason = DETAILS[1]
                    time_afk = get_readable_time(int(return_time-afk_time))
                    if afk_reason == "None":
                        return await m.reply(f"<i>I'm AFK... \n\nSince {time_afk}</i>")
                    return await m.reply(f"<i>I'm AFK... \n\nSince {time_afk}\n\nReason :- {afk_reason}</i>")
            else:
                if m.from_user:
                    hehe = m.text.split()
                    if not un in hehe:
                        return
                    DETAILS = await get_afk_details(id)
                    return_time = time.time()
                    afk_time = DETAILS[0]
                    afk_reason = DETAILS[1]
                    time_afk = get_readable_time(int(return_time-afk_time))
                    if afk_reason == "None":
                        return await m.reply(f"<i>I'm AFK... \n\nSince {time_afk}</i>")
                    return await m.reply(f"<i>I'm AFK... \n\nSince {time_afk}\n\nReason :- {afk_reason}</i>")
