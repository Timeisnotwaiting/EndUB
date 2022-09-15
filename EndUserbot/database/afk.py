from ..build_db import db

afkdb = db.afk

async def add_afk(self_id: int, reason: str, time: str):
    await afkdb.insert_one({"self_id": self_id, "reason": reason, "time": time})

async def del_afk(self_id: int):
    find = await afkdb.find_one({"self_id": self_id})
    reason = find["reason"]
    time = find["time"]
    await afkdb.delete_one({"self_id": self_id, "reason": reason, "time": time})

async def is_afk(self_id: int):
    find = afkdb.find_one({"self_id": self_id})
    if find:
        return True
    return False

async def get_afk_details(self_id: int):
    find = await afkdb.find_one({"self_id": self_id})
    reason = find["reason"]
    time = find["time"]
    return reason, time
