import bcrypt

from lib import error


def compare_hash(string: str, hashed_string: str):
    hash_matches = bcrypt.checkpw(string.encode("utf-8"), hashed_string.encode("utf-8"))
    if hash_matches != True:
        return error.DynErr(err="provided password does not match hashed password")
    return error.DynErr()
