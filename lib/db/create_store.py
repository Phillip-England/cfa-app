from pymongo.collection import Collection
from models import StoreModel, StoreResult


def create_store(store_collection: Collection, store: StoreModel):
    result = store_collection.insert_one(
        {"user": store.user, "name": store.name, "number": store.number}
    )
    store_result = StoreResult(result.inserted_id, store.user, store.name, store.number)
    return store_result
