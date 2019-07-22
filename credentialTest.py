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
        self.new_cred = Credential('instagram','risras', 'natty')
    def tearDown(self):
        """
        Method that does clean up after each test has run.
        """
        Credential.cred_list = []
    def test_init(self):
        """
        Test case to see if the objects are being initialized properly.
        """
        self.assertEqual(self.new_cred.account_name, 'instagram')
        self.assertEqual(self.new_cred.username, 'risras')
        self.assertEqual(self.new_cred.password, 'natty')

    def test_store_existing_cred(self):
        """
        Test case to check whether credentials can be stored in cred_list.
        """
        self.new_cred.save_cred()
        self.assertEqual(len(Credential.cred_list), 1)

    def test_store_multiple_cred(self):
        """
        Test case to check whether multiple credentials can be stored in cred_list.
        """
        self.new_cred.save_cred()
        test_cred = Credential('linkedIn','Risper', 'orissy')
        test_cred.save_cred()
        self.assertEqual(len(Credential.cred_list), 2)
    
    def test_display_cred(self):
        """
        Test case to check if the credentials can be displayed.
        """
        self.assertEqual(Credential.display_cred(), Credential.cred_list)

    def test_copy_cred(self):
        """
        Test to check if credentials are copied to clipboard.
        """
        self.new_cred.save_cred()
        Credential.copy_cred('risras')
        self.assertEqual(pyperclip.paste(), self.new_cred.username)

    