from .utils import eor, get_reply_and_message, verify
from . import Client, Message
import asyncio
from ..database import is_sudo
from pathlib import Path

def conv(s):
    des = s.with_suffix(".webp")
    

async def kang(_, m):
    v = await verify(_, m, m.from_user.id)
    if not v:
        return
    reply, message = await get_reply_and_message(m)
    if not reply in ["sticker", "photo"]:
        return await eor(m, "REPLY TO AN IMAGE OR A STICKER")
