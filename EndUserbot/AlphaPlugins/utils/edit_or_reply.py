from pyrogram.types import Message

async def eor(m: Message, t):
    try:
        await m.edit(t)
    except:
        try:
            await m.delete()
            await m.reply(t)
        except:
            await m.reply(t)
    
