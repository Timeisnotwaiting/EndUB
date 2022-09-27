from . import Client, Message
from .utils import eor
from EndUserbot.database import pm_perm, toggle_pm_perm
from config import COMMAND_HANDLER as hl

async def pm_protect(_, m):
    if not m.from_user.is_self:
        return
    if len(m.command) != 2:
        return await eor(m, f"<code>{hl}pmpermit ON | OFF</code>")
    toggler = m.text.split()[1]
    toggler = toggler.lower()
    if not toggler in ["on", "off"]:
        return await eor(m, f"<code>{hl}pmpermit ON | OFF</code>")
    check = await pm_perm()
    if check:
        if toggler == "on":
            return await eor(m, f"<i>pm protection is already enabled..!</i>")
        await toggle_pm_perm()
        return await eor(m, f"<i>pm protection enabled..!</i>")
    else:
        if toggler == "off":
            return await eor(m, f"<i>pm protection isn't enabled..!</i>")
        await toggle_pm_perm()
        return await eor(m, f"<i>pm protection disabled..!</i>")
