import os
from dotenv import dotenv_values, find_dotenv

env_config = dotenv_values(find_dotenv())

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = None
    WTF_CSRF_ENABLED = False
    
class LocalDevelopmentConfig(Config):
    DEBUG = True
    SQLITE_DB_DIR = os.path.join(basedir,"../db")
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+ os.path.join(SQLITE_DB_DIR,"dev_db.sqlite3")
    SECRET_KEY= env_config['SECRET_KEY']  

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    pass

