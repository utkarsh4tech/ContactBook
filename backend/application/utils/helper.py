from application.data.model import User

def getUser(username):
    user=User.query.filter_by(user_name=username).first()
    return user
