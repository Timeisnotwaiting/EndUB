from ..build_db import db

afkdb = db.afk

async def is_afk(self_id: int):
    self_afk = await afkdb.find_one({"self_id": self_id})
    if not self_afk:
        return False
    return True

async def add_afk(self_id: int, details):
    return await afkdb.update_one({"self_id": self_id}, {"$set": {"details": details}}, upsert=True)

async def remove_afk(self_id: int):
    return await afkdb.delete_one({"self_id": self_id})

async def get_afk_details(self_id: int):
    get = await afkdb.find_one({"self_id": self_id})
    det = get["details"]
    AFK_DETAILS = [det["afk_time"], det["afk_reason"]]
    return AFK_DETAILS
