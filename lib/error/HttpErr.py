from fastapi import Response


class HttpErr(Exception):
    def __init__(self, code: int, msg: str):
        self.code = code
        self.message = msg

    def exit(self, response: Response):
        response.status_code = self.code
        return {"msg": self.message}
