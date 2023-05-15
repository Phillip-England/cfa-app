from bson import ObjectId

from lib import sys


def assert_object_id(some_string: str):
    try:
        ObjectId(some_string)
        return sys.Result()
    except Exception as err:
        return sys.Result().err()
