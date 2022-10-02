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
    xD += f"✥ 𝙊𝙬𝙣𝙚𝙧 :- {men}\n"
    xD += f"✥ 𝙋𝙞𝙣𝙜 :- {str((end-st)*1000)[0:5]}ms\n"
    xD += f"✥ 𝙐𝙗 𝘿𝙚𝙫 :- [ЄƝƊ](t.me/THE_END_NETWORK)\n"
    await m.delete()
    return await m.reply_photo(ALIVE_PIC, caption=xD)
