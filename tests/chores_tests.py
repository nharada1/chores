import chores
import unittest
import json


class ChoresTestCase(unittest.TestCase):
    """Unittests in this module rely on the memory resident database backend"""
    def setUp(self):
        chores.chore_app.testing = True
        self.app = chores.chore_app.test_client()

    def tearDown(self):
        pass

    def test_root(self):
        rv = self.app.get('/')
        assert('Not found' in str(rv.data))

    def test_not_found(self):
        rv = self.app.get('api/wheels/saywhatagainidareyouidoubledareyou')
        assert('requested URL was not found on the server' in str(rv.data))

    def test_create_new(self):
        args = '{"people": ["Nate", "Noelle"], "chores": ["Garbage", "Laundry"], "days_per_rotation": 4}'
        rv = self.app.post('/api/wheels', data=args, content_type='application/json')
        recv = json.loads(rv.data.decode("utf-8"))
        assert('id' in recv)
        assert(type(recv['id']) == str)

if __name__ == "__main__":
    unittest.main()