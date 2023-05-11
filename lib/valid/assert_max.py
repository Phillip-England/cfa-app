from lib.error import DynErr


def assert_max(string: str, max: int):
    if len(string) > max:
        return DynErr("assert max failed")
    return DynErr()
