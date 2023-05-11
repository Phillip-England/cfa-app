import os

from pymongo import MongoClient


class Mongo:
    def __init__(self, client: MongoClient):
        self.client = client
        self.users = client[os.getenv("DB_NAME")]["users"]
        self.sessions = client[os.getenv("DB_NAME")]["sessions"]
        self.stores = client[os.getenv("DB_NAME")]["stores"]
