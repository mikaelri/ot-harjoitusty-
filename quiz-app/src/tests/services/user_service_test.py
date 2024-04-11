import unittest
from entities.user import User
from repositories.user_repository import user_repository
from services.user_service import (
    UserService,
    InvalidCredentialsError,
    UsernameExistsError,
    PasswordError,
    PasswordTooShortError
)


class FakeUserRepository:
    def __init__(self, users=[]):
        self.users = users

    def get_all(self):
        return self.users

    def get_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def create_user(self, user):
        self.users.append(user)

    def delete_all(self):
        self.users = []


class TestUserService(unittest.TestCase):
    def setUp(self):
        fake_user_repository = FakeUserRepository()
        self.user_service = UserService(fake_user_repository)

        fake_user_repository.delete_all()
        self.user_player1 = User("player1", "player1password")

    def test_create_new_user(self):
        username = self.user_player1.username
        password = self.user_player1.password
        password2 = self.user_player1.password
        all_users = self.user_service.get_users()

        self.user_service.create_user(username, password, password2)

        self.assertEqual(len(all_users), 1)
        self.assertEqual(all_users[0].username, username)
        self.assertEqual(all_users[0].password, password)

    def test_creating_same_user_raises_existing_error(self):
        username = self.user_player1.username
        password = self.user_player1.password
        password2 = self.user_player1.password

        self.user_service.create_user(username, password, password2)

        with self.assertRaises(UsernameExistsError):
            self.user_service.create_user(username, password, password2)

    def test_creating_user_with_too_short_username_raises_credentials_error(self):
        with self.assertRaises(InvalidCredentialsError):
            self.user_service.create_user(
                "ab", self.user_player1.password, self.user_player1.password)

    def test_creating_user_with_not_matching_passwords_raises_password_error(self):
        username = self.user_player1.username
        password = self.user_player1.password
        password2 = "wrongpassword"

        with self.assertRaises(PasswordError):
            self.user_service.create_user(username, password, password2)

    def test_creating_user_with_too_short_password_raises_password_error(self):
        username = self.user_player1.username
        password = "short"
        password2 = "short"

        with self.assertRaises(PasswordTooShortError):
            self.user_service.create_user(username, password, password2)

    def test_created_user_can_login(self):
        username = self.user_player1.username
        password = self.user_player1.password
        password2 = self.user_player1.password

        self.user_service.create_user(username, password, password2)
        user = self.user_service.login(username, password)
        self.assertEqual(user.username, username)

    def test_login_conditional_statement_True(self):
        username = self.user_player1.username
        password = self.user_player1.password
        password2 = self.user_player1.password

        self.user_service.create_user(
            username, password, password2, login=True)
        current_user = self.user_service.login(username, password)
        self.assertIsNotNone(current_user.username)

    def test_login_conditional_statement_False(self):
        username = self.user_player1.username
        password = self.user_player1.password
        password2 = self.user_player1.password

        current_user = self.user_service.create_user(
            username, password, password2, login=False)
        self.assertIsNone(current_user)

    def test_returns_current_user(self):
        username = self.user_player1.username
        password = self.user_player1.password
        password2 = self.user_player1.password

        created_user = self.user_service.create_user(
            username, password, password2)
        current_user = self.user_service.get_current_user()

        self.assertEqual(created_user, current_user)

    def test_login_raises_credentials_error(self):
        with self.assertRaises(InvalidCredentialsError):
            self.user_service.login("testuser", "testpassword")

    def test_logout_is_succesful(self):
        username = self.user_player1.username
        password = self.user_player1.password
        password2 = self.user_player1.password

        self.user_service.create_user(username, password, password2)
        self.user_service.login(username, password)
        logout_user = self.user_service.logout()

        self.assertEqual(logout_user, None)
