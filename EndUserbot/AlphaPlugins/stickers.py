from .utils import eor, get_reply_and_message
from . import Client, Message
import asyncio
from ..database import is_sudo
from pathlib import Path
from PIL import Image
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName

def conv(s):
    des = s.with_suffix(".webp")
    I = Image.open(s)
    I.save(des, format="webp")
    return des
    
async def kang(_, m):
    s = await is_sudo(m.from_user.id)
    mine = await _.get_me().id
    if m.from_user.id != mine and not s:
        return
    un = (await _.get_users(mine)).username
    if not un:
        un = mine
    else:
        un += "@" + un
    reply, message = await get_reply_and_message(m)
    if not message:
        emoji = "🤧"
    else:
        emoji = message[0]
    if not reply in ["sticker", "photo"]:
        return await eor(m, "REPLY TO AN IMAGE OR A STICKER")
    pack_name = "[{}]_END-UB_{}_pack"
    if reply == "photo":
        await _.download_media(m.reply_to_message, file_name="END.jpg")
        x = Path("downloads/END.jpg")
        y = conv(x)
        await asyncio.sleep(0.2)
        pn = pack_name.format(un, "kang")
        exist = await _.send(
            GetStickerSet(stickerset=InputStickerSetShortName(short_name=pn))
        )
        if not exist:
            try:
                await _.send_message("stickers", "/newpack")
                await asyncio.sleep(0.2)
                await _.send_message("stickers", un)
                await asyncio.sleep(0.2)
                await _.send_document("stickers", y, force_document=True)
                await asyncio.sleep(0.2)
                await _.send_message("stickers", emoji)
                await asyncio.sleep(0.2)
                await _.send_message("stickers", "/publish")
                await asyncio.sleep(0.2)
                await _.send_message("stickers", "/skip")
                await asyncio.sleep(0.2)
                await _.send_message("stickers", un)
                return await eor(m, f"STICKER KANGED [PACK](https://t.me/addstickers/{pn})")
            except:
                return await eor(m, "ERROR OCCURED")
        else:
            try:
                await _.send_message("stickers", "/addsticker")
                await asyncio.sleep(0.2)
                await _.send_message("stickers", un)
                await asyncio.sleep(0.2)
                await _.send_document("stickers", y, force_document=True)
                await asyncio.sleep(0.2)
                await _.send_message("stickers", emoji)
                await asyncio.sleep(0.2)
                await _.send_message("stickers", "/done")
                return await eor(m, f"STICKER KANGED [PACK](https://t.me/addstickers/{pn})")
            except:
                return await eor(m, "ERROR OCCURED")
    elif reply == "sticker":
        await _.download_media(m.reply_to_message, file_name="END.webp")
        y = "downloads/END.webp"
        pn = pack_name.format(un, "kang")
        exist = await _.send(
            GetStickerSet(stickerset=InputStickerSetShortName(short_name=pn))
        )
        if not exist:
            try:
                await _.send_message("stickers", "/newpack")
                await asyncio.sleep(0.2)
                await _.send_message("stickers", un)
                await asyncio.sleep(0.2)
                await _.send_document("stickers", y, force_document=True)
                await asyncio.sleep(0.2)
                await _.send_message("stickers", emoji)
                await asyncio.sleep(0.2)
                await _.send_message("stickers", "/publish")
                await asyncio.sleep(0.2)
                await _.send_message("stickers", "/skip")
                await asyncio.sleep(0.2)
                await _.send_message("stickers", un)
                return await eor(m, f"STICKER KANGED [PACK](https://t.me/addstickers/{pn})")
            except:
                return await eor(m, "ERROR OCCURED")
        else:
            try:
                await _.send_message("stickers", "/addsticker")
                await asyncio.sleep(0.2)
                await _.send_message("stickers", un)
                await asyncio.sleep(0.2)
                await _.send_document("stickers", y, force_document=True)
                await asyncio.sleep(0.2)
                await _.send_message("stickers", emoji)
                await asyncio.sleep(0.2)
                await _.send_message("stickers", "/done")
                return await eor(m, f"STICKER KANGED [PACK](https://t.me/addstickers/{pn})")
            except:
                return await eor(m, "ERROR OCCURED")
