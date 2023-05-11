from fastapi import Response

from lib import error


class DynErr(BaseException):
    def __init__(self, err: str = None, value: any = None):
        self.err = err
        self.value = value

    def wrap(self, value: any):
        self.value = value
        return self

    def http_unwrap(self, code: int, msg: str):
        if self.value != None:
            return self.value
        else:
            raise error.HttpErr(code, msg)

    def http_err(self, code: int, msg: str):
        if self.err != None:
            raise error.HttpErr(code, msg)
