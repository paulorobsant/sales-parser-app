import sqlalchemy
from databases import Database

DATABASE_URL = "sqlite:///./app.db"

database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
