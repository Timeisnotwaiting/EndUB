from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import config 

def build_db():
    mongo = MongoClient(config.MONGO_DB_URL)
    return mongo.END
