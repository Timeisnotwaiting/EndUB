from . import Client, Message
from .utils import eor
from ..database import is_sudo
import time

async def lmao(_, m):
    A = "😂🤣😂🤣😂🤣😂🤣"
    B = "🤣😂🤣😂🤣😂🤣😂"
    id = m.from_user.id
    reply = m.reply_to_message
    x = await is_sudo(id)
    l = await _.get_me().id
    if not l and not x:
        return
    if reply:
        if m.from_user.is_self:
            ok = await eor(m, A)
        else:
            ok = await reply.reply(m, A)
        time.sleep(1)
        for y in range(0, 10):
            await ok.edit(B)
            time.sleep(1)
            await ok.edit(A)
    else:
        ok = await eor(m, A)
        time.sleep(1)
        for y in range(0, 10):
            await ok.edit(B)
            time.sleep(1)
            await ok.edit(A)
