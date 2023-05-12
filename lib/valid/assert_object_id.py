from bson import ObjectId

from lib import error


def assert_object_id(some_string: str):
    try:
        ObjectId(some_string)
        return error.DynErr()
    except Exception as err:
        return error.DynErr(err="invalid object id")
