import os

import pymongo
from fastapi import FastAPI
from dotenv import load_dotenv

from lib.db import Mongo
from lib.http import mount


load_dotenv()
app = FastAPI()
client = pymongo.MongoClient(os.getenv("MONGO_URI"))
mongo = Mongo(client)
mount(app, mongo)
