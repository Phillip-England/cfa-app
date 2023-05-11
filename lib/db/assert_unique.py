from pymongo.collection import Collection

from lib.error import DynErr


def assert_unique(collection: Collection, filter: dict):
    doc = collection.find_one(filter)
    if doc != None:
        return DynErr("mongo doc already exists")
    return DynErr()
