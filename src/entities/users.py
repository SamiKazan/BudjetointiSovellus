class Users:
    """Class that defines a user.

    Attributes:
        username: String that defines the user username.
        password: String that defines the user password.
    """

    def __init__(self, username, password):
        """Class constructor that creates a new user.

        Args:
            username: String that defines the user username.
            password: String that defines the user password.
        """
        self.username = username
        self.password = password
