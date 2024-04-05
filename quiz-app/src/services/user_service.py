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
    """Class taking care of the application logic for user.
    Attributes:
        user_repository: 
            by default user_repository, has the methods from UserRepository class          
    """

    def __init__(self, user_repository = default_user_repository):
        """ Contructor, creating a new application logic service

        Args:
            user_repository: 
                by default user_repository, has the methods from UserRepository class  
        """
        self._user = None
        self._user_repository = user_repository       

    def login(self, username, password):
        """handles the login for user.
        Args:
            username:
                user's username as a string variable
            password:
                user's password as a string variable
        Returns:
            A new user 
        Raises:
            InvalidCredentialsError:
                Error message if there is not a user with given username.
                Error message if the password does not match the user's password.
        """
        user = self._user_repository.get_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError
        
        self._user = user
        return user

    def get_current_user(self):
        """gets the current user
         Returns:
            Current logged in user
        """
        return self._user
    
    def get_users(self):
        """gets all users
        Returns:
            A list of all users
        """
        return self._user_repository.get_all()
    
    def logout(self):
        """log out the current user"""
        self._user = None

    def create_user(self, username, password, password2, login=True):
        """create a new user
        Args:
            username:
                user's username as a string variable
            password:
                user's password as a string variable
            login:
                Boolean value used to login the user
        Raises:
            UsernameExistsError:
                Error if the username is already taken
        Returns:
            The created user
        """
        current_user = self._user_repository.get_by_username(username)

        if current_user:
            raise UsernameExistsError
        
        if len(username) < 3 or len(username) == 0:
            raise InvalidCredentialsError
        
        if len(password) < 6 or len(password) == 0:
            raise PasswordTooShortError
        
        if password != password2:
            raise PasswordError
         
        user = self._user_repository.create_user(User(username, password))

        if login:
            self._user = user
              
        return user

user_service = UserService()
