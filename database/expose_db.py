from .databases import LocalDB

db = LocalDB()


def get_wheel(id):
    return db.get_wheel(id)


def new_wheel(people, chores, days_per_rotation):
    return db.new_wheel(people, chores, days_per_rotation)
