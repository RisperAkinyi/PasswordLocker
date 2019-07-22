import pyperclip

class Credential:
    """
    Class that creates credentials instances
    """
    cred_list = []

    def __init__(self, account_name, username, password):
        """
        Defines properties for our objects.

        Args:
            account_name: new account_name.
            username: new username.
            password: new password.
        """
        self.account_name = account_name
        self.username = username
        self.password = password

    def save_cred(self):
        """
        Method that stores objects into cred_list.
        """
        self.cred_list.append(self)

    @classmethod
    def display_cred(cls):
        """
        Method that returns the cred_list list
        """
        return cls.cred_list

    @classmethod
    def copy_cred(cls, username):
        """
        Method that copies credentials to clipboard.
        """
        pyperclip.copy(username)


