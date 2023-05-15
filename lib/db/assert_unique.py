from pymongo.collection import Collection

from lib import sys


def assert_unique(collection: Collection, filter: dict):
    doc = collection.find_one(filter)
    if doc != None:
        return sys.Result().err()
    return sys.Result()
