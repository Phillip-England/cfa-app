from fastapi import Request

from lib import error, db


def auth(req: Request, mongo: db.Mongo):
    session_token = req.cookies["session_token"]
    if session_token == "":
        return error.DynErr(
            err="fastapi request cookies does not contain session_token"
        )
    session = db.find_session_by_id(mongo.sessions, session_token)
    user = db.find_user_by_id(mongo.users, session.user)
    return error.DynErr().wrap(user)
