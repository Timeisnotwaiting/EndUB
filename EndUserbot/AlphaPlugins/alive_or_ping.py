from pyrogram import Client
from pyrogram.types import Message
from .utils import eor
import time

async def alive_or_ping(_, m):
    st = time.time()
    await eor(""`Checking...`")
    end = time.time()
    l = await _.get_me()
    men = l.mention
    xD = ""
    xD += f"✥ 𝙊𝙬𝙣𝙚𝙧 :- {men}\n"
    xD += f"✥ 𝙋𝙞𝙣𝙜 :- {str(end-st)}\n"
    xD += f"✥ 𝙐𝙗 𝘿𝙚𝙫 :- [ЄƝƊ](t.me/THE_END_NETWORK)"\n"
    await m.delete()
    return await m.reply_photo(ALIVE_PIC, caption=xD)
