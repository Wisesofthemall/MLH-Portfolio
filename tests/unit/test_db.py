import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]
# Use an in-memory SQLite for tests.
test_database = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):

    def setUp(self):
        test_database.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_database.connect()
        test_database.create_tables(MODELS)

    def tearDown(self):
        test_database.drop_tables(MODELS)
        test_database.close()

    def test_create_post(self):
        first_post = TimelinePost.create(name='Test', email="Test@gmail", content="Hello, I'm test")
        self.assertEqual(first_post.id, 1)
        second_post = TimelinePost.create(name='Test2', email="Test2@gmail", content="Hello, I'm test2")
        self.assertEqual(second_post.id, 2)

if __name__ == '__main__':
    unittest.main()


