import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate

from application.config import LocalDevelopmentConfig
from application.data.database import db
from application.controller.api.userapi import UserApi

def create_app(app=None, api = None):

    app= Flask("Contact Book")

    if os.getenv('ENV',default="development") == "production":
        raise Exception("No production config setup")
    elif os.getenv('ENV',default="development") == "testing":
        raise Exception("No Testing config setup")
    else:
        print("=====    Starting local development    =====")
        app.config.from_object(LocalDevelopmentConfig) 

    with app.app_context():
        db.init_app(app)
        Migrate(app,db)
    
    with app.app_context():
        api=Api(app)
    
    with app.app_context():
        CORS(app)

    return app, api

app,api = create_app()

api.add_resource(UserApi,"/user/<string:username>", "/user")

from application.controller.controllers import *

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)