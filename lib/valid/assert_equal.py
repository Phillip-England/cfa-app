from lib import sys


def assert_equal(value1: any, value2: any):
    if value1 != value2:
        return sys.Result().err()
    return sys.Result()
