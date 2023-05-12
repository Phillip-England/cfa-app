from pymongo.collection import Collection
from bson import ObjectId


def delete_store_by_id(store_collection: Collection, _id: str):
    store_collection.delete_one({"_id": ObjectId(_id)})
