from pyrogram import Client

async def get_me(Client):
    _ = await Client.get_me()
    return _
