from ..database.afk import *
from pyrogram.types import Message
from pyrogram import Client
import time

async def _afk(_: Client, m: Message):
    if not m.from_user.is_self:
        return
    if await is_afk(m.from_user.id):
        await del_afk(m.from_user.id)
        if len(m.command) > 1:
            reason = m.text.split(None, 1)[1]
        else:
            reason = "None"
        time = time.time()
        try:
            await add_afk(m.from_user.id, reason, time)
            if not reason == "None":
                return await eor(m, f"`I shall be Going afk! because ~` {reason}")
            else:
                return await eor(m, f"`I shall be Going afk!)
        except Exception as e:
            return await eor(m, e)


    else:
        if len(m.command) > 1:
            reason = m.text.split(None, 1)[1]
        else:
            reason = "None"
        time = time.time()
        try:
            await add_afk(m.from_user.id, reason, time)
            if not reason == "None":
                return await eor(m, f"`I shall be Going afk! because ~` {reason}")
            else:
                return await eor(m, f"`I shall be Going afk!)
        except Exception as e:
            return await eor(m, e)
