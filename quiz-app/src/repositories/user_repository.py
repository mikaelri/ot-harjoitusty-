from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row: any) -> object:
    """Gets the user in a row, used in mapping all of the user to a list.

    Args:
        row:
            Selected variable for the users table
    Returns:
        A User object in a row, formed in User model from entities or None.
    """

    return User(row["username"], row["password"]) if row else None


class UserRepository:
    """Class taking care of the user related database operations."""

    def __init__(self, connection):
        """Constructor for UserRepository class, handles database changes for the users.

        Args:
            connection: Database object for the connection.
        """

        self._connection = connection

    def get_all(self) -> list:
        """Gets all of the users from the database.

        Returns:
            A list of all users.
        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def get_by_username(self, username: str) -> str:
        """Gets user by username from the database.

        Args:
            username:
                String variable, represents the username for the user object.
        Returns:
            The user object by the username or None.
        """

        cursor = self._connection.cursor()

        cursor.execute("SELECT * from users WHERE username = ?", (username,))
        row = cursor.fetchone()

        return get_user_by_row(row)

    def create_user(self, user: object) -> object:
        """Create a new user and initializes points to the database.

        Args:
            user:
                Object variable of the created new user.

        Returns:
            Created user as user object.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        cursor.execute(
            "INSERT INTO user_stats (username, quiz_points) values (?, ?)",
            (user.username, 0)
        )
        self._connection.commit()

        return user

    def delete_all(self) -> None:
        """Deletes all users from the database."""

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
