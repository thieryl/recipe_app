# project/test/test_recipes.py
import unittest
from project import app


class ProjecTests(unittest.TestCase):
    """
        Setup and Tear Down
    """

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEquals(app.debug, False)

    def tearDown(self):
        pass

    # Main test
    def test_login_page(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertIn(b'Future site for logging into Louison Family Recipes!',
                      response.data)


if __name__ == "__main__":
    unittest.main()
