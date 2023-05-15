from fastapi import Request

from lib import sys, db


def auth(req: Request, mongo: db.Mongo):
    session_token = req.cookies["session_token"]
    if session_token == "":
        return sys.Result().err()
    session = db.find_session_by_id(mongo.sessions, session_token)
    user = db.find_user_by_id(mongo.users, session.user)
    return sys.Result().wrap(user)
