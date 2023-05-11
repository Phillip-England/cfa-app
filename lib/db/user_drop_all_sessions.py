from pymongo.collection import Collection


def user_drop_all_sessions(session_collection: Collection, user_id: str):
    session_collection.delete_many({"user": user_id})
