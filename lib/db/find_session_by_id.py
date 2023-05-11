from pymongo.collection import Collection
from bson import ObjectId

from models import SessionResult


def find_session_by_id(session_collection: Collection, session_id: str):
    result = session_collection.find_one({"_id": ObjectId(session_id)})
    session_result = SessionResult(result["_id"], result["user"])
    return session_result
