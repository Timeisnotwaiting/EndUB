from pyrogram import enums
from gtts import gTTS

def convert(txt):
    tts = gTTS(txt)
    x = "alpha.mp3"
    tts.save(x)
    return x

async def teeteeyess(_, m):
    try:
        await m.delete()
    except:
        pass
    reply = m.reply_to_message
    if not reply:
        if len(m.command) < 2:
            return await m.reply("**Either reply or give some text !**")
    
    if reply:
        if not reply.text and not reply.caption:
            return await m.reply("**No text found in replied messages !**")
        txt = reply.text if reply.text else reply.caption
        path = convert(txt)
    else:
        txt = m.text.split(None, 1)[1]
        path = convert(txt)

    try:
        await _.send_chat_action(m.chat.id, enums.ChatAction.RECORD_AUDIO)
        await m.reply_voice(path)
        await _.send_chat_action(m.chat.id, enums.ChatAction.CANCEL)
    except:
        await _.send_chat_action(m.chat.id, enums.ChatAction.RECORD_AUDIO)
        await m.reply_audio(path)
        await _.send_chat_action(m.chat.id, enums.ChatAction.CANCEL)
