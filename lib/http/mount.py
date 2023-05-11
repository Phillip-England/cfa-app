from fastapi import FastAPI


from lib import db
from routes import user_routes, store_routes


def mount(app: FastAPI, mongo: db.Mongo):
    user_routes(app, mongo)
    store_routes(app, mongo)
