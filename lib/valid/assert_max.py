from lib import sys


def assert_max(string: str, max: int):
    if len(string) > max:
        return sys.Result().err()
    return sys.Result()
