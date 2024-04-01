from flask_login import UserMixin

from .database import db


# User model
class User(db.Model, UserMixin):

    __tablename__ = "USER"
    user_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    firstname = db.Column(db.String,nullable=False)
    lastname =  db.Column(db.String,nullable=True)
    user_name = db.Column(db.String,nullable=False,unique=True)
    hashed_password = db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False,unique=True)
    phn_number=db.Column(db.String, nullable=False,unique=True)