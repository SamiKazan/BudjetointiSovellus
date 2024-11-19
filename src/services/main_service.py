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

        if self.user_repo.find(username):
            raise "Username already in use"

        user = self.user_repo.create_account(Users(username, password))

        return user
    
budgeting_service = BudgetingService()

