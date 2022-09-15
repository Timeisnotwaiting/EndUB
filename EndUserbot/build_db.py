from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import config 

mongo = MongoClient(config.MONGO_DB_URL)

db = mongo.END
