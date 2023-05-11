from lib.error import DynErr


def assert_min(string: str, min: int):
    if len(string) < min:
        return DynErr("assert min failed")
    return DynErr()
