from . import Client, Message
from .utils import eor
from ..database import is_sudo
from PIL import Image, ImageFont, ImageDraw
import os

def DrawSize(file_name):
    x = Image.open(file_name)
    size = x.size
    return size

async def mmf(_, m):
    id = m.from_user.id
    sd = await is_sudo(id)
    x = await _.get_me()
    i = x.id
    if not sd and id != i:
        return
    reply, message = await get_reply_and_message(_, m)
    if not reply in ["photo", "sticker"]:
        return await eor(m, "REPLY TO A STICKER OR AN IMAGE !!")
    if not message:
        return await eor(m, "GIVE SOME TEXT TO DO SO !!")
