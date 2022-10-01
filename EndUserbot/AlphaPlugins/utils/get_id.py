from pyrogram.types import Message

async def get_id(m: Message):
    if str(m.chat.id)[0] != "-":
        return int(m.chat.id)
    if not m.reply_to_message:
        text = m.text.split()
        un_or_id = text[1]
        if un_or_id[0] == "@":
            id = (await _.get_users(un_or_id)).id
        else:
            id = int(un_or_id)
    else:
        id = m.reply_to_message.from_user.id
    return id 
