from pymongo.collection import Collection

from lib import error
from models import UserResult


def find_user_by_email(user_collection: Collection, email: str):
    result = user_collection.find_one({"email": email})
    if result == None:
        return error.DynErr(err="could not find user by email")
    user = UserResult(result["_id"], result["email"], result["password"])
    return error.DynErr().wrap(user)
