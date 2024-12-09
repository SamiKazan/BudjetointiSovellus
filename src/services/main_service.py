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
        self.user = None
        self.user_repo = user_repo
        self.budget_repo = budget_repo

    def create_account(self, username, password):
        """Creates new account

        Args:
            username: string, users' username
            password: string, users' password
        Returns:
            user if successs
            None if username is already taken
        """
        user_exists = self.user_repo.find(username)

        if user_exists:
            print("Username already in use (Main)")
            return None
            
        user = self.user_repo.create_account(Users(username, password))

        self.user = user

        print("User created (Main)")
        return user

    def login(self, username, password):
        """Logs user in

        Args:
            username: string, users' username
            password: string, users' password
        Returns:
            Logged in user object
        Raises:
            todo...
        """

        user = self.user_repo.find(username)

        if not user or password != user.password:
            print("invalid username or password (Main)")
            return None

        self.user = user
        print("Logged in as", self.user.username, "(Main)")
        return user

    def logout(self):
        """Logs user out
        """
        self.user = None

    def create_budget(self, content):
        """Creates new budget

        Args:
            content: dictionary of budget info
        Returns:
            budget: budget in form of Budgets class
        Raises:
            todo...
        """
        if not self.user:
            print("No user logged in")
            return None

        budget = self.budget_repo.create_budget(Budgets(self.user.username, content["name"],
                                                        content["income"], content["rent"],
                                                        content["bills"], content["hobbies"],
                                                        content["misc"]))

        print("Budget created (Main)")
        return budget

    def get_budgets(self):
        """Gets users' budgets
        
        Returns:
            list of budgets in Budgets class form
        """
        if not self.user:
            return []

        budgets = self.budget_repo.find_budgets(self.user.username)

        return list(budgets)
    
    def delete_budget(self, budget_id):
        """Deletes budget

        Args:
            budget_id: string(uuid), id of specific budget
        Raises:
            todo...
        """        
        if not self.user:
            return
        
        self.budget_repo.delete_budget(budget_id)
        print("deletion successful")

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


budgeting_service = BudgetingService()
