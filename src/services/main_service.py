from entities.users import Users
from entities.budgets import Budgets
from repositories.user_repo import user_repository
from repositories.budgeting_repo import budget_repository


class BudgetingService:
    """App logic"""

    def __init__(
            self,
            user_repo=user_repository,
            budget_repo=budget_repository):

        self.user = None
        self.user_repo = user_repo
        self.budget_repo = budget_repo

    def create_account(self, username, password):
        """Creates new account"""

        user_exists = self.user_repo.find(username)

        if user_exists:
            print("Username already in use (Main)")
            return None
            
        user = self.user_repo.create_account(Users(username, password))

        self.user = user

        print("User created (Main)")
        return user

    def login(self, username, password):
        """Logs user into app"""

        user = self.user_repo.find(username)

        if not user or password != user.password:
            print("invalid username or password (Main)")
            return None

        self.user = user
        print("Logged in as", self.user.username, "(Main)")
        return user

    def logout(self):
        self.user = None

    def create_budget(self, content):
        """Creates new budget"""
        if not self.user:
            print("No user logged in")
            return None

        budget = self.budget_repo.create_budget(Budgets(self.user.username, content["name"],
                                                        content["income"], content["rent"],
                                                        content["groceries"], content["hobbies"],
                                                        content["misc"]))

        print("Budget created (Main)")
        return budget

    def get_budgets(self):
        """Gets users budgets"""
        if not self.user:
            return []

        budgets = self.budget_repo.find_budgets(self.user.username)

        return list(budgets)


budgeting_service = BudgetingService()
