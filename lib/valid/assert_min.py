from lib import sys


def assert_min(string: str, min: int):
    if len(string) < min:
        return sys.Result().err()
    return sys.Result()
