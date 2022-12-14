from . import Client, Message
from .utils import eor, get_id
from EndUserbot.database import pm_perm, toggle_pm_perm, is_approved, toggle_approve, warn_user, get_pm_warns, reset_warns
from config import COMMAND_HANDLER as hl

async def pm_protect(_, m):
    if not m.from_user.is_self:
        return
    check = await pm_perm()
    if check:
        xD = "ON"
    else:
        xD = "OFF"
    if len(m.command) != 2:
        return await eor(m, f"<code>{hl}pmpermit ON | OFF\n\nStatus :- {xD}</code>")
    toggler = m.text.split()[1]
    toggler = toggler.lower()
    if not toggler in ["on", "off"]:
        return await eor(m, f"<code>{hl}pmpermit ON | OFF\n\nStatus :- {xD}</code>")
    if check:
        if toggler == "on":
            return await eor(m, f"<i>pm protection is already enabled..!</i>")
        await toggle_pm_perm()
        return await eor(m, f"<i>pm protection disabled..!</i>")
    else:
        if toggler == "off":
            return await eor(m, f"<i>pm protection isn't enabled..!</i>")
        await toggle_pm_perm()
        return await eor(m, f"<i>pm protection enabled..!</i>")

async def pm_cwf(_, m):
    check = await pm_perm()
    if not check:
        return
    if str(m.chat.id)[0] == "-":
        return 
    check_user = await is_approved(m.chat.id)
    if check_user:
        return
    await warn_user(m.chat.id)
    w = await get_pm_warns(m.chat.id)
    await m.reply(f"{w}")
    if w == 3:
        await _.block_user(m.chat.id)
        await reset_warns(m.chat.id)
    

async def approve_disapprove(_, m):
    if not m.from_user.is_self:
        return
    try:
        if str(m.chat.id)[0] == "-":
            id = await get_id(m)
        else:
            id = m.chat.id
    except:
        return await eor(m, f"<i>{hl}a | {hl}da [ID | USERNAME | REPLY]</i>")
    approved = await is_approved(id)
    if m.text.split()[0][1].lower() == "d":
        if not approved:
            return await eor(m, f"<i>user wasn't approved..!</i>")
        await toggle_approve(id)
        return await eor(m, f"<i>user disapproved..!</i>")
    else:
        if approved:
            return await eor(m, f"<i>user is already approved...!</i>")
        await toggle_approve(id)
        await reset_warns(id)
        return await eor(m, f"<i>user approved..!</i>")
        
