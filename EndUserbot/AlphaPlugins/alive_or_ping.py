from pyrogram import Client
from pyrogram.types import Message
from .utils import eor
import time
from config import ALIVE_PIC
from ..database import is_sudo

async def alive_or_ping(_, m):
    sudo = await is_sudo(m.from_user.id)
    l = await _.get_me()
    my_id = l.id
    if not m.from_user.id == my_id and not sudo:
        return
    st = time.time()
    await eor(m, "`Checking...`")
    end = time.time()
    men = l.mention
    xD = ""
    xD += f"β₯ ππ¬π£ππ§ :- {men}\n"
    xD += f"β₯ πππ£π :- {str((end-st)*1000)[0:5]}ms\n"
    xD += f"β₯ ππ πΏππ« :- [ΠΖΖ](t.me/THE_END_NETWORK)\n"
    await m.delete()
    return await m.reply_photo(ALIVE_PIC, caption=xD)
