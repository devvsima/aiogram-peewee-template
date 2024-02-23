from peewee import PostgresqlDatabase, SqliteDatabase,Model
from data.config import db_name, db_host ,db_port, db_user, db_password, DIR

if db_name and db_host and db_port and db_user and db_password:
    db = PostgresqlDatabase(db_name, host=db_host, port=db_port, user=db_user, password=db_password)
else:
    db = SqliteDatabase(f"{DIR}/database/db.sqlite3")
db.connect()

class BaseModel(Model):
    class Meta:
        database = db