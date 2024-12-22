import unittest
from repositories.user_repo import user_repository
from repositories.budgeting_repo import budget_repository
from entities.users import Users
from entities.budgets import Budgets
from initialize_database import initialize_database


class TestBudgetingRepo(unittest.TestCase):
    def setUp(self):
        initialize_database()
        user_repository.delete_all_accounts()
        self.user1 = Users('testi1', 'testi1')
        self.budget1 = Budgets(self.user1.username, "test_budget", 1000,
                               500, 200, 100, 100)
        self.budget2 = Budgets(self.user1.username, "test_budget2", 1000,
                               100, 200, 100, 100)

    def test_create_budget(self):
        budget_repository.create_budget(self.budget1)

        find = budget_repository.find_budgets(self.user1.username)

        self.assertEqual(len(find), 1)

    def test_delete_budget(self):
        budget_repository.create_budget(self.budget1)
        budget_repository.create_budget(self.budget2)
        find = budget_repository.find_budgets(self.user1.username)

        self.assertEqual(len(find), 2)

        budget_repository.delete_budget(self.budget2.id)

        find2 = budget_repository.find_budgets(self.user1.username)

        self.assertEqual(len(find2), 1)
