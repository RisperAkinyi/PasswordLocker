import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User class behaviours.
    '''

    def setUp(self):
        """
        Method to run before the test cases.
        """
        self.new_user = User('Risper', 'Akinyi', 'risras', 'natty')

    def test_init(self):
        """
        Test case to see if the object is being initialized properly.
        """
        self.assertEqual(self.new_user.first_name, 'Risper')
        self.assertEqual(self.new_user.last_name, 'Akinyi')
        self.assertEqual(self.new_user.username, 'risras')
        self.assertEqual(self.new_user.password, 'natty')

    def test_save_user(self):
        """
        Test case to see if objects are being stored on user_list.
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1