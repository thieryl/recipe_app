# project/test/test_recipes.py
import os
import unittest
from project import app, db

TEST_DB = 'test.db'


class ProjecTests(unittest.TestCase):
    """
        Setup and Tear Down
    """

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(app.config['BASEDIR'], TEST_DB)
        app.config['DEBUG'] = False
        self.app = app.test_client()
        db.create_all()

        self.assertEquals(app.debug, False)

    def tearDown(self):
        pass

    # Main test
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(
            b'Louison Family Recipes', response.data)
        self.assertIn(b'Breakfast Recipes', response.data)
        self.assertIn(b'Lunch Recipes', response.data)
        self.assertIn(b'Dinner Recipes', response.data)
        self.assertIn(b'Dessert Recipes', response.data)

    # Main page query result
    def test_main_page_query_results(self):
        response = self.app.get('/add', follow_redirects=True)
        self.assertIn(b'Add a New Recipes', response.data)

    # add Valid recipe
    def test_add_recipe(self):
        response = self.app.post(
            '/add',
            data=dict(recipe_title='Hamburgers',
                      recipe_description='Delicious Hamburgers with pretzel rolls'),
            follow_redirects=True)
        self.assertIn(b'New recipe, Hamburgers, added!', response.data)

    def test_add_recipes(self):
        response = self.app.post(
            '/add',
            data=dict(recipe_title='Hamburgers',
                      recipe_description='Delicious hamburger with pretzel rolls'),
            follow_redirects=True)
        self.assertIn(b'New recipe, Hamburgers, added!', response.data)

    # add Invalid recipe

    def test_add_invalid_recipe(self):
        response = self.app.post('/add',
                                 data=dict(recipe_title='',
                                           recipe_description='Delicious Hamburgers with pretzel rolls'),
                                 follow_redirects=True)
        self.assertIn(b'This field is required.', response.data)


if __name__ == "__main__":
    unittest.main()
