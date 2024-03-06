from ..connect import db_users

async def get_user(id):
    return db_users.find_one({"_id":id})

async def add_user(id):
    if await get_user(id) is None:
        return db_users.insert_one({"_id":id})

async def get_or_create_user(id):
    user = await get_user(id)
    if user: return user
    else: add_user(id)