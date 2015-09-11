import uuid
import pymongo
import os
from datetime import datetime


class Database(object):
    def __int__(self):
        self.init_connection()

    def init_connection(self):
        pass

    def get_wheel(self, wheel_id):
        """Return a wheel if it exists in the database

        Arguments
        ---------
        wheel_id : string
            Unique ID for the wheel

        Returns
        -------
        found_wheel : dict
            A valid wheel in dict form, or None if not found
        """
        pass

    def new_wheel(self, people, chores, days_per_rotation):
        """Create a new wheel in the database. Requires that people and chores are the
        same length, this should be done server-side

        Arguments
        ---------
        people : list
            List of people (list of strings)

        chores : list
            List of chores (list of strings)

        days_per_rotation : int
            How often to rotate the wheel
        """
        if len(people) != len(chores):
            raise ValueError('People and chores must be the same length')


class LocalDB(Database):
    def __init__(self):
        """Local DB is for testing, uses a simple dict for basically all storage"""
        self.db = {}
        self.init_connection()
        super(LocalDB, self).__init__()

    def init_connection(self):
        pass

    def get_wheel(self, wheel_id):
        if wheel_id in self.db:
            return self.db[wheel_id]
        else:
            return None

    def new_wheel(self, people, chores, days_per_rotation):
        super(LocalDB, self).new_wheel(people, chores, days_per_rotation)
        cur_day = datetime.now().isoformat()
        wheel = {'people': people, 'chores': chores, 'days_per_rotation': days_per_rotation, 'date_created': cur_day}
        new_id = str(uuid.uuid1())
        self.db[new_id] = wheel
        return new_id


class MongoDB(Database):
    def __init__(self):
        """MongoDB bindings for production"""
        self.uri = os.environ.get('MONGOLAB_URI')
        self.wheels = None
        self.init_connection()
        super(MongoDB, self).__init__()

    def init_connection(self):
        client = pymongo.MongoClient(self.uri)
        default_db = client.get_default_database()
        self.wheels = default_db.wheels

    def new_wheel(self, people, chores, days_per_rotation):
        super(MongoDB, self).new_wheel(people, chores, days_per_rotation)
        cur_day = datetime.now().isoformat()
        new_id = str(uuid.uuid1())
        wheel = {'people': people, 'chores': chores, 'days_per_rotation': days_per_rotation, 'date_created': cur_day, '_id': new_id}
        returned_id = self.wheels.insert_one(wheel).inserted_id
        return returned_id

    def get_wheel(self, wheel_id):
        searched = self.wheels.find_one({'_id': wheel_id})
        return searched
