from PIL import Image
from pathlib import Path
from . import Client, Message
from EndUserbot.database import is_sudo
from .utils import eor, get_reply_and_message
import time

def conv(s):
    des = s.with_suffix(".jpg")
    i = Image.open(s)
    i.save(des, format="webp")
    return des

async def kang(_, m):
    id = m.from_user.id
    s = m.from_user.is_self
    c = await is_sudo(id)
    if not s and not c:
        return
    stickers = None
    if not stickers:
        stickers = (await _.get_users("stickers")).id
    try:
        await _.archive_chats(stickers)
    except:
        pass
    if not m.reply_to_message:
        return await eor(m, "REPLY TO A STICKER OR AN IMAGE..")
    reply, message = await get_reply_and_message(m)
    if reply == "photo":
        if message:
            emoji = message[0]
        else:
            emoji = "🤧"
        await _.download_media(m.reply_to_message, file_name="END.jpg")
        x = conv(Path("downloads/END.jpg"))
        await _.send_message("stickers", "/addsticker")
        time.sleep(2)
        
    
