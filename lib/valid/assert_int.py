from lib import error


def assert_int(value: any):
    try:
        int(value)
        return error.DynErr()
    except Exception as err:
        return error.DynErr("cannot convert value to int")
