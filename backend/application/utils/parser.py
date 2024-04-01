from flask_restful import reqparse

# creating a parser for adding new user , method=POST
user_parser=reqparse.RequestParser()
user_parser.add_argument("firstname")
user_parser.add_argument("lastname")
user_parser.add_argument("username")
user_parser.add_argument("password")
user_parser.add_argument("email")

# creating a parser for editing user , method=PUT
update_user_parser=reqparse.RequestParser()
update_user_parser.add_argument("firstname")
update_user_parser.add_argument("lastname")
update_user_parser.add_argument("password")
