# project/test/test_recipes.py
import os
import unittest

from project import app, db

TEST_DB = 'user.db'


class ProjecTests(unittest.TestCase):
    """
        Setup and Tear Down
    """

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CRSF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        self.assertEquals(app.debug, False)

    def tearDown(self):
        pass

    def register(self, email, password, confirm):
        return self.app.post('register/',
                             data=dict(email=email,
                                       password=password,
                                       confirm=confirm),
                             follow_redirects=True
                             )

    # Main test
    def test_login_page(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertIn(b'Future site for logging into Louison Family Recipes!',
                      response.data)

    # Test user registration page displays the right information
    def test_user_registration_display(self):
        response = self.app.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please Register Your New Account', response.data)

    # Test Valid user
    def test_valid_user_registration(self):
        self.app.get('/register', follow_redirects=True)
        response = self.register(
            'example@example.com', 'FlaskIsAwesome', 'FlaskIsAwesome')
        self.assertIn(b'Thanks for registering!', response.data)

    # Test Duplicate user's mail
    def test_duplicate_email_user_registration(self):
        self.app.get('/register', follow_redirects=True)
        response = self.register(
            'example@example.com', 'FlaskIsAwesome', 'FlaskIsAwesome')
        self.app.get('/register', follow_redirects=True)
        self.assertIn(
            b'ERROR! Email (example@example.com) already exists.', response.data)

    # Test missing field
    def test_missing_field_user_registration(self):
        self.app.get('/register', follow_redirects=True)
        response = self.register(
            'example@example.com', 'FlaskIsAwesome', '')
        self.assertIn(b'This field is required.', response.data)


if __name__ == "__main__":
    unittest.main()
