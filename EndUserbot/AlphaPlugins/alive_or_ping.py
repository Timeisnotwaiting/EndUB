from pyrogram import Client
from pyrogram.types import Message
from .utils import eor
import time
from config import ALIVE_PIC, SUDO_USERS

async def alive_or_ping(_, m):
    V = SUDO_USERS.copy()
    l = await _.get_me()
    V.append(l.id)
    if not m.from_user.id in V:
        return
    st = time.time()
    await eor(""`Checking...`")
    end = time.time()
    men = l.mention
    xD = ""
    xD += f"✥ 𝙊𝙬𝙣𝙚𝙧 :- {men}\n"
    xD += f"✥ 𝙋𝙞𝙣𝙜 :- {str(end-st)}\n"
    xD += f"✥ 𝙐𝙗 𝘿𝙚𝙫 :- [ЄƝƊ](t.me/THE_END_NETWORK)"\n"
    await m.delete()
    return await m.reply_photo(ALIVE_PIC, caption=xD)
