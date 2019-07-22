import unittest
from credential import Credential
import pyperclip

class TestCredential(unittest.TestCase):
    """
    Defines test cases for the credentials class behaviours.

    Args:
        TestCase: A class that helps create the test cases.
    """

    def setUp(self):
        """
        Method that runs before the test cases.
        """
        self.new_cred = Credential('github','Lugaga', 'tangodown!')
    def tearDown(self):
        """
        Method that does clean up after each test has run.
        """
        Credential.cred_list = []
    def test_init(self):
        """
        Test case to see if the objects are being initialized properly.
        """
        self.assertEqual(self.new_cred.account_name, 'github')
        self.assertEqual(self.new_cred.username, 'Lugaga')
        self.assertEqual(self.new_cred.password, 'tangodown!')
