from fastapi import Response

from . import HttpErr


def http_pipe(err: Exception, res: Response):
    if isinstance(err, HttpErr):
        res.status_code = err.code
        return {"msg": err.message}
    res.status_code = 500
    return {"msg": str(err)}
