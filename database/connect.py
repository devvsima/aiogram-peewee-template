from pymongo import MongoClient
from data.config import mongodb_url

client = MongoClient(mongodb_url)
db = client["name"]

coll_users = db.users

