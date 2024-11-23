import unittest
from repositories.user_repo import user_repository
from services.main_service import budgeting_service
from entities.users import Users
from initialize_database import initialize_database


class TestBudgetservice(unittest.TestCase):
    def setUp(self):
        initialize_database()
        user_repository.delete_all_accounts()

    def test_create_account(self):
        budgeting_service.create_account('testi2', 'testi2')

        is_user = user_repository.find('testi2')

        self.assertNotEqual(is_user, None)

    def test_login_logout(self):
        budgeting_service.create_account('testi', 'testi')

        budgeting_service.login('testi', 'testi')

        self.assertEqual(budgeting_service.user.username, 'testi')

        budgeting_service.logout()

        self.assertEqual(budgeting_service.user, None)
