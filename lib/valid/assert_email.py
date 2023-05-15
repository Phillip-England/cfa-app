import re
from lib import sys


def assert_email(string: str) -> sys.Result:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, string) == None:
        return sys.Result().err()
    return sys.Result()
