from ..build_db import db

pmdb = db.pm

async def pm_perm():
    on = pmdb.find_one({"pm_perm": 1})
    if not on:
        return False
    return True

async def toggle_pm():
    is_on = await pm_perm()
    if not is_on:
        return await pmdb.insert_one({"pm_perm": 1})
    if is_on:
        return await pmdb.delete_one({"pm_perm": 1})
    
