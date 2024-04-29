import unittest
from repositories.user_repository import user_repository
from repositories.question_repository import question_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        question_repository.delete_all_user_points()

        self.user_player1 = User("player1", "player1password")
        self.user_player2 = User("player2", "player2password")

    def create_user(self, user):
        return user_repository.create_user(user)

    def test_create_user_finds_correct_user(self):

        user = self.create_user(self.user_player1)
        all_users = user_repository.get_all()

        self.assertEqual(len(all_users), 1)
        self.assertEqual(all_users[0].username, user.username)

    def test_create_user_doesnt_find_not_created_user(self):
        user = self.create_user(self.user_player1)
        all_users = user_repository.get_all()
        not_created_user = "player3"

        self.assertEqual(len(all_users), 1)
        self.assertNotEqual(user.username, not_created_user)

    def test_create_user_finds_correct_user_password(self):
        user = self.create_user(self.user_player1)
        all_users = user_repository.get_all()

        self.assertEqual(all_users[0].password, user.password)

    def test_create_user_doesnt_find_not_created_user_password(self):
        user = self.create_user(self.user_player1)
        not_created_user = User("testing", "testing123")

        self.assertNotEqual(user.password, not_created_user.password)

    def test_get_all_returns_correct_user_amount_for_0_users(self):
        all_users = user_repository.get_all()
        self.assertEqual(len(all_users), 0)

    def test_get_all_returns_correct_user_amount_for_users(self):
        user = self.create_user(self.user_player1)
        user2 = self.create_user(self.user_player2)
        all_users = user_repository.get_all()

        self.assertEqual(len(all_users), 2)
        self.assertEqual(all_users[0].username, user.username)
        self.assertEqual(all_users[1].username, user2.username)

    def test_get_by_username_returns_correct_user(self):
        user = self.create_user(self.user_player1)
        user2 = self.create_user(self.user_player2)
        retrieved_user = user_repository.get_by_username(user.username)

        self.assertEqual(user.username, retrieved_user.username)
        self.assertNotEqual(user2.username, retrieved_user.username)

    def test_delete_all_returns_0_users(self):
        self.create_user(self.user_player1)
        self.create_user(self.user_player2)

        all_users = user_repository.get_all()
        user_repository.delete_all()
        all_users = user_repository.get_all()

        self.assertEqual(len(all_users), 0)
