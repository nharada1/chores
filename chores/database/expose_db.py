from .databases import LocalDB, MongoDB
import os

if 'ON_HEROKU' in os.environ:
    db = MongoDB()
else:
    db = LocalDB()


def get_wheel(id):
    return db.get_wheel(id)


def new_wheel(people, chores, days_per_rotation):
    return db.new_wheel(people, chores, days_per_rotation)
