# project/test/test_recipes.py
import unittest
from project import app


class ProjecTests(unittest.TestCase):
    """
        Setup and Tear Down
    """

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()

        self.assertEquals(app.debug, False)

    def tearDown(self):
        pass

    # Main test
