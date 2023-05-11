from fastapi import Response


def success(response: Response, code: int, data: dict = None):
    response.status_code = code
    if data != None:
        return {"msg": "success", "data": data}
    return {"msg": "success"}
