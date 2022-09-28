from . import Client, Message
from .utils import eor, get_id
from config import COMMAND_HANDLER as hl


async def block_or_unblock_user(_, m):
    if not m.from_user.is_self:
        return
    try:
        id = await get_id(m)
    except:
        return await eor(m, f"<i>{hl}block | {hl}unblock [ID | USERNAME | REPLY]</i>")
    if m.text.split()[0][1].lower() == "b":
        await _.block_user(id)
        return await eor(f"<i>user blocked..!</i>")
    else:
        await _.unblock_user(id)
        return await eor(f"<i>user unblocked..!</i>")
        
