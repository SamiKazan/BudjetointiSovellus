from entities.users import Users
from database_connection import get_database_connection


def get_user_by_row(row):
    return Users(row["username"], row["password"]) if row else None

class UserRepository:
    """
    Class for database related to user operations
    """
    def __init__(self, connection):
        """Class constructor

        ARGS:
            connection: Connection to databse
        """
        self._connection = connection

    def create_account(self, user):
        """Creates new user account

        Args:
            user: An instance of the Buser class containing username and password

        returns:
            user
        """
        d_b = self._connection.cursor()

        d_b.execute("insert into users (username, password) values (?,?)",
                    (user.username, user.password))

        self._connection.commit()
        print("user", user.username, "created to DB")
        return user

    def delete_account(self, username):
        """Deletes user account

        Args:
            username: string, users' username
        """
        d_b = self._connection.cursor()

        d_b.execute("delete from users where username = ?", (username,))

        self._connection.commit()

    def delete_all_accounts(self):
        """Deletes all accounts
        """
        d_b = self._connection.cursor()

        d_b.execute("delete from users")

        self._connection.commit()

    def find(self, username):
        """Finds specific user

        Args:
            username: string, users' username

        returns:
            user: username and password
        """
        d_b = self._connection.cursor()

        d_b.execute(
            "select * from users where username = ?",
            (username,))

        row = d_b.fetchone()
        return get_user_by_row(row)


user_repository = UserRepository(get_database_connection())
