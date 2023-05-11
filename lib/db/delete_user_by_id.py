from bson import ObjectId

from lib import db


def delete_user_by_id(mongo: db.Mongo, user_id: str):
    mongo.users.delete_one({"_id": ObjectId(user_id)})
    mongo.sessions.delete_many({"user": ObjectId(user_id)})
