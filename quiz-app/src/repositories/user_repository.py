import sqlite3
from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row) -> object:
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all(self) -> list:
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def get_by_username(self, username) -> str:
        cursor = self._connection.cursor()

        cursor.execute("SELECT * from users WHERE username = ?", (username,))
        row = cursor.fetchone()

        return get_user_by_row(row)

    def create_user(self, user) -> object:
        cursor = self._connection.cursor()
        try:
            self._connection.execute("BEGIN")
            cursor.execute(
                "INSERT INTO users (username, password) values (?, ?)",
                (user.username, user.password)
            )

            cursor.execute(
                "INSERT INTO user_stats (username, quiz_points) values (?, ?)",
                (user.username, 0)
            )
            self._connection.commit()
            return user

        except sqlite3.IntegrityError as error:
            self._connection.rollback()
            raise ValueError(f"Could not create user: {str(error)}") from error
        except Exception as error:
            self._connection.rollback()
            raise RuntimeError(f"An error occurred: {str(error)}") from error

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
