import bcrypt

from lib import sys


def compare_hash(string: str, hashed_string: str):
    hash_matches = bcrypt.checkpw(string.encode("utf-8"), hashed_string.encode("utf-8"))
    if hash_matches != True:
        return sys.Result().err()
    return sys.Result()
