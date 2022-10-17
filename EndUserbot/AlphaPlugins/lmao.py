from . import Client, Message
from .utils import eor
from ..database import is_sudo
import time

async def lmao(_, m):
    A = "😂🤣😂🤣😂🤣"
    B = "🤣😂🤣😂🤣😂"
    id = m.from_user.id
    reply = m.reply_to_message
    x = await is_sudo(id)
    lx = await _.get_me()
    l = lx.id
    if not l and not x:
        return
    if reply:
        if m.from_user.is_self:
            ok = await m.edit(A)
        else:
            ok = await reply.reply(A)
        time.sleep(0.5)
        for y in range(0, 10):
            await ok.edit(B)
            time.sleep(0.5)
            await ok.edit(A)
            time.sleep(0.5)
    else:
        if m.from_user.is_self:
            ok = await m.edit(A)
        else:
            ok = await m.reply(A)
        time.sleep(0.5)
        for y in range(0, 10):
            await ok.edit(B)
            time.sleep(0.5)
            await ok.edit(A)
            time.sleep(0.5)
