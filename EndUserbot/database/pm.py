from ..build_db import db

pmdb = db.pm

async def pm_perm():
    on = pmdb.find_one({"pm_perm": 1})
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
    hehe = await pmdb.find_one({"user_id": user_id})
    if not hehe:
        return 0
    else:
        warns = hehe["warns"]
        return int(warns)

async def warn_user(user_id: int):
    lmao = await get_pm_warns(user_id)
    await pmdb.delete_one({"user_id"})
    lmao = lmao + 1
    return await pmdb.insert_one({"user_id": user_id}, {"$set": {"warns": lmao}})
