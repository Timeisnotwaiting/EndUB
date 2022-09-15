from pyrogram import Client
from pyrogram.types import Message
from ..database import setlog, get_log
from .utils import eor
from config import COMMAND_HANDLER as hl


async def backup(_, m):
    me = await _.get_me()
    if m.from_user.id != me.id:
        return
    try:
        LOG = await get_log()
    except:
        return await eor(m, f"<i>Set log group first..! Use {hl}setlog < group id></i>")
    if str(m.chat.id)[0] == "-":
        return await eor(m, "Only can backup private chats...")
    await eor(m, "Backing up chat.....")
    ch = _.get_chat_history(m.chat.id)
    MSG_ID = []
    ok = await m.reply("getting history....")
    t_st = time.time()
    try:
        async for i in ch:
            MSG_ID.append(i.id)
    except:
        await ok.edit(f"got {len(MSG_ID)}\n\nsleeping for 10s..")
        await asyncio.sleep(10)
    MSG_ID.reverse()
    t_end = time.time()
    itt = str(t_end-t_st).index(".")
    tt = str(t_end-t_st)[0:itt]
    await eor(m, f"{len(MSG_ID)} messages found...\n\ntime taken :- {tt}s")
    b = 0
    a = 0
    n = len(MSG_ID)//50
    per = len(MSG_ID)//100
    percent = 0
    ST = time.time()
    for id in MSG_ID:
        try:
            await _.forward_messages(LOG, m.chat.id, id)
            a += 1
            b += 1
        except FloodWait as e:
            flood_time = 10
            await ok.edit(f"sleeping for {flood_time}s..")
            await asyncio.sleep(flood_time)
        except:
            pass
        END = time.time()
        CLIn = str(END-ST).index(".")
        CLI = str(END-ST)[0:CLIn]
        if per == a:
            percent += 1
            try:
                await ok.edit(f"{b} messages backed up.....\n\n[ {percent}% ] [ {CLI}s ]")
            except:
                pass
            a = 0
    await ok.delete()
    LVL = time.time()
    PTI= str(LVL-ST).index(".")
    PT = str(LVL-ST)[0:PTI]
    return await eor(m, f"all msges backed up successfully...\n\nTime Elapsed :- {PT}s")

async def set_log(_, m):
    me = await _.get_me()
    if m.from_user.id != me.id:
        return
    try:
        id = int(m.text.split()[1])
    except:
        return await eor(m, f"<i>{hl}setlog : chat id :</i>")
    return await setlog(id), await eor(m, f"<i>Log chat set successfully..!</i>")

    
     
