from ..build_db import db

pmdb = db.pm

pma = db.pm_approve

pmw = db.pmw

async def pm_perm():
    on = await pmdb.find_one({"pm_perm": 1})
    if not on:
        return False
    return True

async def toggle_pm_perm():
    is_on = await pm_perm()
    if not is_on:
        return await pmdb.insert_one({"pm_perm": 1})
    if is_on:
        return await pmdb.delete_one({"pm_perm": 1})

async def get_pm_warns(user_id: int):
    getter = await pmw.find_one({"user_id": user_id})
    if not getter:
        return 0
    return int(getter["warns"])

async def warn_user(user_id: int):
    warns = await get_pm_warns(user_id)
    if warns != 0:
        await pmw.delete_one({"user_id": user_id})
    warns += 1
    await pmw.insert_one({"user_id": user_id}, {"$set": {"warns": warns}}) 

async def reset_warns(user_id: int):
    try:
        await pmw.delete_one({"user_id": user_id})
    except:
        pass   

async def is_approved(user_id: int):
    app = await pma.find_one({"user_id": user_id})
    if app:
        return True
    return False

async def toggle_approve(user_id: int):
    is_app = await is_approved(user_id)
    if is_app:
        return await pma.delete_one({"user_id": user_id})
    else:
        return await pma.insert_one({"user_id": user_id})
