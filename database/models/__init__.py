from .users import Users
from ..connect import db


db.create_tables([Users])