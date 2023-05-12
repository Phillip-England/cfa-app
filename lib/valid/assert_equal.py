from lib import error


def assert_equal(value1: any, value2: any):
    if value1 != value2:
        return error.DynErr(err="values do not match")
    return error.DynErr()
