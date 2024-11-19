import unittest
from repositories.user_repo import user_repository
from entities.users import Users
from initialize_database import initialize_database

class TestUserRepo(unittest.TestCase):
    def setUp(self):
        initialize_database()
        user_repository.delete_all_accounts()
        self.user1 = Users('testi1', 'testi1')
        self.user2 = Users('testi2', 'testi2')

    def test_create_account(self):
        user_repository.create_account(self.user1)

        check = user_repository.find(self.user1.username)

        self.assertEqual(check.username, 'testi1')

    def test_delete_account(self):
        user_repository.create_account(self.user2)

        check = user_repository.find(self.user2.username)

        self.assertEqual(check.username, 'testi2')

        asd = user_repository.delete_account(self.user2.username)

        self.assertEqual(asd, None)
