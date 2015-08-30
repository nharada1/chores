import chores
import unittest


class ChoresTestCase(unittest.TestCase):
    """Unittests in this module rely on the memory resident database backend"""
    def setUp(self):
        chores.chores.testing = True
        self.app = chores.chores.test_client()

    def tearDown(self):
        pass

    def test_root(self):
        rv = self.app.get('/')
        assert('Not found' in str(rv.data))

    def test_not_found(self):
        rv = self.app.get('api/wheels/saywhatagainidareyouidoubledareyou')
        assert('requested URL was not found on the server' in str(rv.data))

    def test_create_new(self):
        args = "'people': ['Vincent', 'Jules', 'Mia'], 'chores': ['Cook', 'Clean', 'Water Plants'], 'days_per_rotation': 3}"
        rv = self.app.post('/api/wheels', data=args, content_type='application/json')
        print(rv.__dict__)
        #import pdb; pdb.set_trace()

if __name__ == "__main__":
    unittest.main()