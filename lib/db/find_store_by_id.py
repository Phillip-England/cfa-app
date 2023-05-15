from pymongo.collection import Collection

from bson import ObjectId

from models import StoreResult
from lib import sys


def find_store_by_id(store_collection: Collection, id: str):
    result = store_collection.find_one({"_id": ObjectId(id)})
    if result == None:
        return sys.Result().err()
    store_result = StoreResult(
        result["_id"], result["user"], result["name"], result["number"]
    )
    return sys.Result().wrap(store_result)
