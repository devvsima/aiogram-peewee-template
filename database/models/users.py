from peewee import TextField, IntegerField, Model, CharField, BigIntegerField
from ..connect import db, BaseModel


class Users (BaseModel):
   id=BigIntegerField(primary_key=True)
   role=CharField(default='user')

db.create_tables([Users])