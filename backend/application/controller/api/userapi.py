from flask_restful import Resource
from werkzeug.security import generate_password_hash

from application.data.model import User
from application.data.database import db
from application.utils.validation import ValidationError
from application.utils.parser import *
from application.utils.helper import getUser

class UserApi(Resource):

    def get(self,username):
        
        user=getUser(username)
        
        if user:
            return {
                "userid": user.user_id,
                "username": user.user_name,
                "firstname":user.firstname,
                "lastname":user.lastname,
                "email": user.email,
                "Phone Number": user.phn_number 
                }, 200
        else:
            raise ValidationError(404,"UVE1006","Such user does not exist")

    def put(self,username):
        user=User.query.filter_by(user_name=username).first()
        if user is None:
            raise ValidationError(404,"UVE1006","Such user does not exist")
        else:
            args=update_user_parser.parse_args()
            firstname,lastname,password=args.get("firstname",None),args.get("lastname",None),args.get("password",None)
            if (firstname is None) or (firstname=='') :
                raise ValidationError(404,"UVE1001","Firstname is  required")
            elif password is None or (password==''):
                raise ValidationError(404,"UVE1003","Password is required")
            elif len(password)<8 or len(password)>20:
                raise ValidationError(404,"UVE1005","Password must be between 8 to 20 characters")
            else:            
                password=generate_password_hash(password)
                user.firstname,user.lastname,user.hashed_password=firstname,lastname,password
                db.session.commit()
                return {"new_fname":firstname,
                        "new_lname":lastname},200

    def delete(self,username):
        user=User.query.filter_by(user_name=username).first()
        if user is None:
            raise ValidationError(404,"UVE1006","Such user does not exist")
        elif len(user.decks)>0:
            raise ValidationError(404,"UVE1007","User has decks,Delete them first!")
        else:
            db.session.delete(user)
            db.session.commit()
            return {"deleteduser_id":user.user_id,
                    "deleteduser_fname":user.firstname,
                    "deleteduser_lname":user.lastname,
                    "deleteduser_username":user.user_name},200

    def post(self):
        args=user_parser.parse_args()
        firstname,lastname,username,password,email=args.get("firstname",None),args.get("lastname",None),args.get("username",None),args.get("password",None),args.get("email",None)
        if firstname is None or (firstname=='') :
            raise ValidationError(404,"UVE1001","Firstname is  required")
        elif username is None or (username=='') :
            raise ValidationError(404,"UVE1002","Username is  required")
        elif password is None or (password==''): 
            raise ValidationError(404,"UVE1003","Password is required")
        elif email is None or ("@" not in email) :
            raise ValidationError(404,"UVE1008","Email is required")
        elif User.query.filter_by(user_name=username).first()  is not None:
            raise ValidationError(404,"UVE1004","Username already exists")
        elif User.query.filter_by(email=email).first() is not None:
            raise ValidationError(404,"UVE1009","Email already exists")
        elif len(password)<8 or len(password)>20:
            raise ValidationError(404,"UVE1005","Password must be between 8 to 20 characters")
        else:
            newuser=User(user_name = username, hashed_password = generate_password_hash(password),firstname = firstname, lastname = lastname,email=email )
            db.session.add(newuser)
            db.session.commit()
            return {"newuserid":newuser.user_id,
                    "newuser_fname":newuser.firstname,
                    "newuser_lname":newuser.lastname,
                    "newuser_username":newuser.user_name,
                    "message":"New User Added Successfully"},201