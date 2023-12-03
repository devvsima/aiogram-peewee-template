from .base import User

def get_user(id):
    return User(id=id)


def add_user(id, name):
    newUsr = User.create(id=id, name=name)

    
