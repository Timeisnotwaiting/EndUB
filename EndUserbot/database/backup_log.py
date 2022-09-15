from ..build_db import db

logdb = db.log

async def setlog(chat_id: int):
    umm = logdb.find({"chat_id": {"$lt": 0}})
    if umm:
        log = []
        for _ in await umm.to_list(length=1000000000):
            log.append(_["chat_id"])
        for id in log:
            await logdb.delete_one({"chat_id": id})
    return await logdb.insert_one({"chat_id": chat_id})

