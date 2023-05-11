from pymongo.collection import Collection

from models import UserResult, UserModel


def insert_user(user_model: UserModel, user_collection: Collection):
    result = user_collection.insert_one(
        {"email": user_model.email, "password": user_model.password}
    )
    user_result = UserResult(result.inserted_id, user_model.email, user_model.password)
    return user_result
