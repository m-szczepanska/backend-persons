from models import Person, Location, sqlite_db


def create_tables():
    with sqlite_db:
        sqlite_db.create_tables([Person, Location])
