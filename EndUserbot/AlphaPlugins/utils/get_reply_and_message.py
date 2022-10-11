from .. import Message

async def get_reply_and_message(m: Message):
    text = m.text.split(None, 1)[1]
    r = m.reply_to_message
    if r:
        if r.photo:
            if len(m.command) > 1:
                message = text
            else:
                message = None
            return "photo", message
        elif r.sticker:
            if len(m.command) > 1:
                message = None
            else:
                message = None
            return "sticker", message
        elif r.video:
            if len(m.command) > 1:
                message = text
            else:
                message = None
            return "video", message
        elif r.audio:
            if len(m.command) > 1:
                message = text
            else:
                message = None
            return "audio", message
        elif r.document:
            if len(m.command) > 1:
                message = text
            else:
                message = None
            return "document", message
