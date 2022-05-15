import unittest
from entities.user import User
from entities.record import Record
from repositories.user_repository import user_repository
from repositories.record_repository import record_repository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = user_repository
        self.user_repository.delete_all_users()

        self.record_repository = record_repository
        self.record_repository.delete_all_records_from_all_users()

        self.user = User("user A", "qwerty")
        self.record = Record(1, 1, 1, 1, 1, 1, self.user.username)

    def test_create_user(self):
        new_user = self.user_repository.create_user(self.user)
        self.assertEqual(new_user, "User created")

    def test_find_user(self):
        self.user_repository.create_user(self.user)
        user = self.user_repository.find_user(self.user.username)
        self.assertEqual((user.username, user.password),
                         (self.user.username, self.user.password))

    def test_user_not_found(self):
        user = self.user_repository.find_user(self.user.username)
        self.assertEqual(user, None)

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

    def test_add_record(self):
        self.user_repository.create_user(self.user)
        add = self.record_repository.add_record(self.record)
        self.assertEqual(add, "Record added")

    def test_show_all_records(self):
        self.user_repository.create_user(self.user)
        self.record_repository.add_record(self.record)
        show_all = self.record_repository.show_all_records(
            self.record.username)
        amount = len(show_all)
        self.assertEqual(amount, 1)

    def test_delete_all_records(self):
        self.user_repository.create_user(self.user)
        self.record_repository.add_record(self.record)
        delete = self.record_repository.delete_all_records(
            self.record.username)
        self.assertEqual(delete, "All records deleted")

