import unittest
from repositories.user_repo import user_repository
from repositories.budgeting_repo import budget_repository
from entities.users import Users
from entities.budgets import Budgets
from initialize_database import initialize_database


class TestUserRepo(unittest.TestCase):
    def setUp(self):
        initialize_database()
        user_repository.delete_all_accounts()
        self.user1 = Users('testi1', 'testi1')
        self.budget1 = Budgets(self.user1.username, "test_budget", 1000,
                               500, 200, 100, 100)

    def test_create_budget(self):
        budget_repository.create_budget(self.budget1)

        find = budget_repository.find_budgets(self.user1.username)

        self.assertEqual(len(find), 1)
