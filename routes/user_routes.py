import datetime

from fastapi import FastAPI, Request, Response
from pydantic import BaseModel


from models import UserModel, UserResponse, SessionModel
from lib import db, error, http, hash, middleware, valid


def user_routes(app: FastAPI, mongo: db.Mongo):
    class ReqCreateUser(BaseModel):
        email: str
        password: str

    @app.post("/user")
    def create_user(b: ReqCreateUser, req: Request, res: Response):
        try:
            valid.assert_email(b.email).http_err(400, "invalid email")
            valid.assert_min(b.password, 5).http_err(400, "password too short")
            valid.assert_max(b.password, 64).http_err(400, "password too long")
            user_model = UserModel(b.email, hash.hash_string(b.password))
            db.assert_unique(mongo.users, {"email": user_model.email}).http_err(
                400, "user already exists"
            )
            user_result = db.insert_user(user_model, mongo.users)
            user_response = UserResponse(user_result._id, user_result.email)
            return http.success(res, 201, user_response.__dict__())
        except Exception as err:
            return error.http_pipe(err, res)

    class ReqLoginUser(BaseModel):
        email: str
        password: str

    @app.post("/user/login")
    def login_user(b: ReqLoginUser, req: Request, res: Response):
        try:
            user = db.find_user_by_email(mongo.users, b.email).http_unwrap(
                400, "invalid credentials"
            )
            hash.compare_hash(b.password, user.password).http_err(
                400, "invalid credentials"
            )
            session_model = SessionModel(user._id)
            db.user_drop_all_sessions(mongo.sessions, user._id)
            session_result = db.insert_session(mongo.sessions, session_model)
            cookie_expiration = datetime.datetime.now() + datetime.timedelta(days=1)
            res.set_cookie(
                key="session_token",
                value=session_result._id,
                expires=cookie_expiration.isoformat(),
            )
            return http.success(res, 200)
        except Exception as err:
            return error.http_pipe(err, res)

    @app.get("/user")
    def get_user(req: Request, res: Response):
        try:
            user = middleware.auth(req, mongo).http_unwrap(401, "unauthorized")
            user_response = UserResponse(user._id, user.email)
            return http.success(res, 200, user_response.__dict__())
        except Exception as err:
            return error.http_pipe(err, res)

    @app.get("/user/logout")
    def logout_user(req: Request, res: Response):
        try:
            user = middleware.auth(req, mongo).http_unwrap(401, "unauthorized")
            db.user_drop_all_sessions(mongo.sessions, user._id)
            res.set_cookie(key="session_token", value="")
            return http.success(res, 200)
        except Exception as err:
            return error.http_pipe(err, res)

    @app.delete("/user")
    def delete_user(req: Request, res: Response):
        try:
            user = middleware.auth(req, mongo).http_unwrap(401, "unauthorized")
            db.delete_user_by_id(mongo, user._id)
            res.set_cookie(key="session_token", value="")
            return http.success(res, 200)
        except Exception as err:
            return error.http_pipe(err, res)
