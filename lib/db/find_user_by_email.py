from pymongo.collection import Collection

from lib import sys
from models import UserResult


def find_user_by_email(user_collection: Collection, email: str):
    result = user_collection.find_one({"email": email})
    if result == None:
        return sys.Result().err()
    user = UserResult(result["_id"], result["email"], result["password"])
    return sys.Result().wrap(user)
