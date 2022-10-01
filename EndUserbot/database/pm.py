from ..build_db import db

pmdb = db.pm

pma = db.pm_approve

pmw = db.pm_warns

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
    hehe = await pmw.find_one({"user_id": user_id})
    if not hehe:
        return False, None
    return True, hehe["warns"]
    

async def warn_user(user_id: int):
    lmao, count = await get_pm_warns(user_id)
    if lmao:
        current = count
    else:
        current = 0
    current += 1
    try:
        await pmw.delete_one({"user_id": user_id})
    except:
        pass
    return await pmw.insert_one({"user_id": user_id}, {"$set": {"warns": current}})

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
