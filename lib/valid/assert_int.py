from lib import sys


def assert_int(value: any):
    try:
        int(value)
        return sys.Result()
    except Exception as err:
        return sys.Result().err()
