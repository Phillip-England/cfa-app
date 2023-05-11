import re
from lib import error


def assert_email(string: str) -> error.DynErr:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, string) == None:
        return error.DynErr("invalid email")
    return error.DynErr()
