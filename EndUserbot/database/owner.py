from ..build_mongo import db

ownerdb = db.owner

async def append_owner(owner_id: int):
    c = ownerdb.find_one({"owner_id": owner_id})
    if not c:
        return await ownerdb.insert_one({"owner_id": owner_id})
    return

async def owner(id: int):
    c = ownerdb.find_one({"owner_id": id})
    if c:
        return True
    return False
