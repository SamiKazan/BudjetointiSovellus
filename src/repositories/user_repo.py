from entities.users import Users
from database_connection import get_database_connection

def get_user_by_row(row):
    return Users(row["username"], row["password"]) if row else None

class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_account(self, user):
        db = self.connection.cursor()

        db.execute("insert into users (username, password) values (?,?)", (user.username, user.password))

        self.connection.commit()

        return user
    
    def delete_account(self, username):
        db = self.connection.cursor()

        db.execute("delete from users where username = ?", (username,))

        self.connection.commit()

    def delete_all_accounts(self):
        db = self.connection.cursor()

        db.execute("delete from users")

        self.connection.commit()

    def find(self, username):
        db = self.connection.cursor()

        db.execute(
            "select * from users where username = ?",
            (username,))

        row = db.fetchone()

        return get_user_by_row(row)


user_repository = UserRepository(get_database_connection())