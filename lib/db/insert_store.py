from pymongo.collection import Collection
from bson import ObjectId

from models import StoreModel, StoreResult


def insert_store(store_collection: Collection, store: StoreModel):
    result = store_collection.insert_one(
        {"user": ObjectId(store.user), "name": store.name, "number": store.number}
    )
    store_result = StoreResult(result.inserted_id, store.user, store.name, store.number)
    return store_result
