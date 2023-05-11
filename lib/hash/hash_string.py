import bcrypt


def hash_string(string: str):
    salt = bcrypt.gensalt()
    string_bytes = string.encode()
    return bcrypt.hashpw(string_bytes, salt).decode("utf-8")
