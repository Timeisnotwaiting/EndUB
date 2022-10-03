from . import Client, Message
import time
from .utils import eor
from config import COMMAND_HANDLER as hl
from ..database import is_sudo

async def type(_, m):
    check = await is_sudo(m.from_user.id)
    l = await _.get_me()
    id = l.id
    if not m.from_user.id == id and not check:
        return
    if len(m.command) < 2:
        return await eor(m, f"{hl}TYPE TEXT") 
    txt = m.text.split(None, 1)[1]
    if m.from_user.is_self:
        msg = ""
        for x in txt:
            msg += x
            await m.edit(msg)
            time.sleep(1)
        
