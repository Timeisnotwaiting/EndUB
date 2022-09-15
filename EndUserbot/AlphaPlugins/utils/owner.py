from .details import get_me
from pyrogram.types import Message
from pyrogram import Client

async def owner(_: Client, m: Message):
    xD = await get_me(_)
    if m.from_user.id == xD.id:
        return True
    return False
