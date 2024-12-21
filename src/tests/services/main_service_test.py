import unittest
from repositories.user_repo import user_repository
from services.main_service import budgeting_service
from entities.users import Users
from entities.budgets import Budgets
from initialize_database import initialize_database


class TestBudgetservice(unittest.TestCase):
    def setUp(self):
        initialize_database()
        user_repository.delete_all_accounts()
        budgeting_service.create_account('testi100', 'testi100')

    def test_create_account(self):
        budgeting_service.create_account('testi2', 'testi2')

        is_user = user_repository.find('testi2')

        self.assertNotEqual(is_user, None)

    def test_login_logout(self):
        budgeting_service.create_account('testi', 'testi')

        budgeting_service.login('testi', 'testi')

        self.assertEqual(budgeting_service._user.username, 'testi')

        budgeting_service.logout()

        self.assertEqual(budgeting_service._user, None)

    def test_user_exists(self):
        budgeting_service.create_account('testi2', 'testi2')
        exists = budgeting_service.create_account('testi2', 'testi2')

        self.assertEqual(exists, None)

    def test_invalid_login(self):
        budgeting_service.create_account('testi', 'testi')

        invalid = budgeting_service.login('testi', 'itset')

        self.assertEqual(invalid, None)

    def test_create_budget(self):
        content = {
            "name": "test_budget",
            "income": 1000,
            "rent": 500,
            "bills": 200,
            "hobbies": 100,
            "misc": 100
        }
  
        no_user = budgeting_service.create_budget(content)
        self.assertEqual(no_user, None)

    def test_create_budget_no_user(self):
        budgeting_service.logout()
        content = {
            "name": "test_budget",
            "income": 1000,
            "rent": 500,
            "bills": 200,
            "hobbies": 100,
            "misc": 100
        }
  
        no_user = budgeting_service.create_budget(content)
        self.assertEqual(no_user, None)

    def test_get_budgets_and_delete(self):
        budgeting_service.login("testi100", "testi100")
        content = {
            "name": "test_budget",
            "income": 1000,
            "rent": 500,
            "bills": 200,
            "hobbies": 100,
            "misc": 100
        }
        budgeting_service.create_budget(content)

        get_budgets = budgeting_service.get_budgets()

        self.assertEqual(len(get_budgets), 1)

        first = get_budgets[0].id
        budgeting_service.delete_budget(first)

        self.assertEqual(len(budgeting_service.get_budgets()), 0)

    def test_get_budgets_no_user(self):
        budgeting_service.logout()

        no_budgets = budgeting_service.get_budgets()

        self.assertEqual(no_budgets, [])

    def test_delete_budget_no_user(self):
        budgeting_service.logout()
        no_user = budgeting_service.delete_budget(1)

        self.assertEqual(no_user, None)

    def test_show_difference(self):
        budgeting_service.login("testi100", "testi100")
        content = {
            "name": "test_budget",
            "income": 1000,
            "rent": 500,
            "bills": 200,
            "hobbies": 100,
            "misc": 100
        }
        budgeting_service.create_budget(content)
        get_budgets = budgeting_service.get_budgets()

        first = get_budgets[0]
        difference = budgeting_service.show_difference(first)

        self.assertEqual(difference, 100.0)
        

    def test_get_user(self):
        budgeting_service.login("testi100", "testi100")
        user = budgeting_service.get_user()
        self.assertEqual("testi100", user)

    def test_get_user_none(self):
        budgeting_service.logout()
        user = budgeting_service.get_user()
        self.assertEqual(None, user)