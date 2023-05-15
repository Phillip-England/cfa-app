import datetime

from fastapi import FastAPI, Request, Response
from bson import ObjectId
from pydantic import BaseModel


from models import StoreModel
from lib import db, error, http, middleware, valid


def store_routes(app: FastAPI, mongo: db.Mongo):
    class ReqCreateStore(BaseModel):
        name: str
        number: str

    @app.post("/store")
    def create_store(b: ReqCreateStore, req: Request, res: Response):
        try:
            user = middleware.auth(req, mongo).unwrap(
                error.HttpErr(401, "unauthorized")
            )
            valid.assert_min(b.name, 3).unwrap(error.HttpErr(400, "name too short"))
            valid.assert_max(b.name, 64).unwrap(error.HttpErr(400, "name too long"))
            valid.assert_min(b.number, 3).unwrap(error.HttpErr(400, "number too short"))
            valid.assert_max(b.number, 64).unwrap(error.HttpErr(400, "number too long"))
            valid.assert_int(b.number).unwrap(
                error.HttpErr(400, "must provide a valid number")
            )
            store_model = StoreModel(user._id, b.name, b.number)
            print(
                db.assert_unique(
                    mongo.stores, {"user": ObjectId(user._id), "name": b.name}
                ).unwrap(error.HttpErr(400, "you already have a store with this name"))
            )

            db.assert_unique(
                mongo.stores, {"user": ObjectId(user._id), "number": b.number}
            ).unwrap(error.HttpErr(400, "you already have a store with this number"))
            store_result = db.insert_store(mongo.stores, store_model)
            return http.success(res, 201, data=store_result.__dict__())
        except Exception as err:
            return error.http_pipe(err, res)

    @app.get("/store")
    def get_stores(req: Request, res: Response):
        try:
            user = middleware.auth(req, mongo).unwrap(
                error.HttpErr(401, "unauthorized")
            )
            stores = db.get_all_user_stores(mongo.stores, user._id)
            for store in stores:
                print(store)
            return http.success(res, 200)
        except Exception as err:
            return error.http_pipe(err, res)

    @app.delete("/store/{id}")
    def delete_store_by_id(req: Request, res: Response, id: str):
        try:
            user = middleware.auth(req, mongo).unwrap(
                error.HttpErr(401, "unauthorized")
            )
            valid.assert_object_id(id).unwrap(400, "invalid id")
            store_result = db.find_store_by_id(mongo.stores, id).unwrap(
                error.HttpErr(400, "invalid id")
            )
            valid.assert_equal(store_result.user, user._id).unwrap(
                error.HttpErr(403, "forbidden")
            )
            db.delete_store_by_id(mongo.stores, id)
            return http.success(res, 200)
        except Exception as err:
            return error.http_pipe(err, res)
