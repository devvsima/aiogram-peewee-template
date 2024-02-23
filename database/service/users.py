from ..models.users import Users


def add_user(user_id) -> None:
    if not find_user:
        Users.create(id=user_id)

def find_user(user_id) -> bool:
    return Users.get(Users.id == user_id).exists()

def get_user(user_id):
    return Users.select().where(Users.id == user_id)

