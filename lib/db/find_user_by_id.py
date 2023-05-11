from pymongo.collection import Collection
from bson import ObjectId

from models import UserResult


def find_user_by_id(user_collection: Collection, user_id: str):
    result = user_collection.find_one({"_id": ObjectId(user_id)})
    user = UserResult(result["_id"], result["email"], result["password"])
    return user
