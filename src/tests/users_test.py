import unittest
from entities.user import User
from repositories.user_repository import user_repository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = user_repository
        self.user_repository.delete_all_users()
        self.user = User("aa", "11", 0)


    def test_create_user(self):
        new_user = self.user_repository.create_user(self.user)
        self.assertEqual(new_user, "User created")


    def test_find_user(self):
        self.user_repository.create_user(self.user)
        user = self.user_repository.find_user(self.user.username)
        self.assertEqual((user.username, user.password, user.calculator),
                         (self.user.username, self.user.password, self.user.calculator))


    def test_find_all_users(self):
        self.user_repository.create_user(self.user)
        users = self.user_repository.find_all_users()
        amount = len(users)
        self.assertEqual(amount, 1)

    def test_delete_user(self):
        self.user_repository.create_user(self.user)
        delete = self.user_repository.delete_user(self.user.username)
        self.assertEqual(delete, "User deleted")

    def test_delete_all_users(self):
        self.user_repository.create_user(self.user)
        delete = self.user_repository.delete_all_users()
        self.assertEqual(delete, None)
