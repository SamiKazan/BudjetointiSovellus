from entities.users import Users
from entities.budgets import Budgets
from repositories.user_repo import user_repository
from repositories.budgeting_repo import budget_repository


class BudgetingService:
    """App logic class
    """

    def __init__(
            self,
            user_repo=user_repository,
            budget_repo=budget_repository):
        """Class constructor. creates instance of applogic

        Args:
            user_repo:
                UserRepository object.
                object has UserRepository classes methods
            budget_repo:
                BudgetRepository object.
                object has Budgetpository classes methods
        """
        self._user = None
        self.user_repo = user_repo
        self.budget_repo = budget_repo

    def create_account(self, username, password):
        """Creates new account

        Args:
            username: string, users' username
            password: string, users' password
        Returns:
            _user if successs
            None if username is already taken
        """
        user_exists = self.user_repo.find(username)

        if user_exists:
            return None

        user = self.user_repo.create_account(Users(username, password))

        self._user = user

        return user

    def login(self, username, password):
        """Logs user in

        Args:
            username: string, users' username
            password: string, users' password
        Returns:
            Logged in _user object
        Raises:
            todo...
        """

        user = self.user_repo.find(username)

        if not user or password != user.password:
            return None

        self._user = user
        return user

    def logout(self):
        """Logs user out
        """
        self._user = None

    def create_budget(self, content):
        """Creates new budget

        Args:
            content: dictionary of budget info
        Returns:
            budget: budget in form of Budgets class
        Raises:
            todo...
        """
        if not self._user:
            return None

        budget = self.budget_repo.create_budget(Budgets(self._user.username, content["name"],
                                                        content["income"], content["rent"],
                                                        content["bills"], content["hobbies"],
                                                        content["misc"]))
        return

    def get_budgets(self):
        """Gets users' budgets

        Returns:
            list of budgets in Budgets class form
        """
        if not self._user:
            return []

        budgets = self.budget_repo.find_budgets(self._user.username)

        return list(budgets)

    def delete_budget(self, budget_id):
        """Deletes budget

        Args:
            budget_id: string(uuid), id of specific budget
        Raises:
            todo...
        """
        if not self._user:
            return

        self.budget_repo.delete_budget(budget_id)
        return

    def show_difference(self, budget):
        """Shows income after expenses

        Args:
            budget: dictionary of budget info
        Returns:
            difference: float, income minus expenses
        """
        expenses = budget.rent + budget.bills + budget.hobbies + budget.misc
        difference = float(budget.income - expenses)

        return difference

    def get_user(self):
        if not self._user:
            return
        return self._user.username


budgeting_service = BudgetingService()
