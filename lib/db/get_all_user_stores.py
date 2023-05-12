from pymongo.collection import Collection


def get_all_user_stores(store_collection: Collection, user_id: str):
    store_docs = store_collection.find({"user": user_id})
    return store_docs
