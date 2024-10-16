from ..models.users import Users
from utils.logging import logger


def get_user(id):
    try:
        return Users.get(Users.id == id)
    except:
        return None

def get_or_create_user(id: int, username: str = None, language: str = "ru") -> Users:
    user = get_user(id)

    if user:
        return user

    return create_user(id, username, language)

def create_user(id: int, username: str = None, language: str = None) -> Users:
    logger.info(f"New user {username} | {id}")
    new_user = Users.create(id=id, username=username, language=language)
    return new_user
