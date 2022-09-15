from EndUserbot.database.owner import append_owner
from pyrogram.types import Message
from pyrogram import Client

async def load_owner(_: Client):
    xD = await _.get_me()
    id = xD.id
    return await append_owner(id)
    
