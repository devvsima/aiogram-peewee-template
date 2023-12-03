from peewee import *
from datetime import datetime


db = SqliteDatabase('database/database.sqlite')
# db.create_tables()
class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id = BigIntegerField(primary_key=True)
    name = CharField(default=None)

    class Meta:
        table_name = 'users'
User.create_table()