from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def get_by_username(self, username):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * from users WHERE username = ?", (username,))
        row = cursor.fetchone()

        return get_user_by_row(row)

    def create_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) values (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()

        return user

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
