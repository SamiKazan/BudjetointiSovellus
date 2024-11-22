from entities.users import Users
from repositories.user_repo import user_repository


class BudgetingService:
    """App logic"""

    def __init__(
            self,
            user_repo=user_repository):

        self.user = None
        self.user_repo = user_repo


    def create_account(self, username, password):
        """Creates new account"""

        user_exists = self.user_repo.find(username)

        if user_exists:
            raise ValueError ("Username already in use mainservice")

        user = self.user_repo.create_account(Users(username, password))
        self.user = user
        print("mainservice menee läpi")
        return user
    

    def login(self, username, password):
        """Logs user into app"""

        user = self.user_repo.find(username)

        if not user or password != user.password:
            print("invalid username or password")

        self.user = user
        print("pääsit jotenkin sisään")
        return user


    def logout(self):
        self.user = None


budgeting_service = BudgetingService()
