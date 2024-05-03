from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class PasswordError(Exception):
    pass


class PasswordTooShortError(Exception):
    pass


class UserService:
    """Class taking care of the application logic for the user."""

    def __init__(self, user_repository=default_user_repository):
        """ Contructor for UserService class, handles user related application logic and creates 
        a new user object.

        Args:
            user_repository: 
                By default user_repository.
                Object, which has the methods from UserRepository class.  
        """

        self._user = None
        self._user_repository = user_repository

    def login(self, username, password) -> object:
        """handles the login for user.

        Args:
            username:
                user's username as a string variable.
            password:
                user's password as a string variable.
        Returns:
            A new user as object.
        Raises:
            InvalidCredentialsError:
                Error message if there is not a user created yet with given username.
                Error message if the password does not match the user's password.
        """

        user = self._user_repository.get_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError

        self._user = user
        return user

    def get_current_user(self) -> object:
        """gets the current user

         Returns:
            Current logged in user
        """

        return self._user

    def get_users(self) -> list:
        """gets all users

        Returns:
            A list of all users
        """

        return self._user_repository.get_all()

    def logout(self):
        """log out the current user."""

        self._user = None

    def create_user(self, username: str, password: str, password2: str, login=True) -> object:
        """creates a new user.

        Args:
            username:
                user's username as a string variable.
            password:
                user's password as a string variable.
            login:
                Boolean value used to login the user.
        Returns:
            The created user as object.
        Raises:
            UsernameExistsError:
                Error if the username is already taken.
            InvalidCredentialsError:
                Error if the username is too short.
            PasswordTooShortError:
                Error if the password is too short.
            PasswordError:
                Error if the password and password2 does not match
        """

        current_user = self._user_repository.get_by_username(username)

        if current_user:
            raise UsernameExistsError

        if not username.strip() or len(username.strip()) < 3:
            raise InvalidCredentialsError

        if not password.strip() or len(password.strip()) < 6:
            raise PasswordTooShortError

        if password.strip() != password2.strip():
            raise PasswordError

        user = self._user_repository.create_user(User(username, password))

        if login:
            self._user = user

        return user


user_service = UserService()
