from .connect import coll_users

async def get_user(id):
    return coll_users.find_one({"_id":id})

async def add_user(id):
    if await get_user(id) is None:
        return coll_users.insert_one({"_id":id})
