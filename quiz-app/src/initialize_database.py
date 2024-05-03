from database_connection import get_database_connection


def drop_tables(connection):
    """Deletes the tables from the database schema.

    Args:
        connection: 
            object to use as connection for the application.
    """

    cursor = connection.cursor()

    cursor.execute("DROP TABLE if exists users;")
    cursor.execute("DROP TABLE if exists questions;")
    cursor.execute("DROP TABLE if exists user_stats;")

    connection.commit()


def create_table_users(connection):
    """Creates the user table to the database schema.

    Args:
        connection: 
            object to use as connection for the application.
    """

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE users (
            username TEXT PRIMARY KEY NOT NULL,
            password TEXT NOT NULL
            );
    """)

    connection.commit()


def create_table_user_stats(connection):
    """Creates the user_stats table to the database schema.

    Args:
        connection: 
            object to use as connection for the application.
    """

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE user_stats(
            username INTEGER NOT NULL,
            quiz_points INTEGER DEFAULT 0,
            highscore INTEGER DEFAULT 0,
            FOREIGN KEY(username) REFERENCES users(username)
            );
    """)

    connection.commit()


def create_table_questions(connection):
    """Creates the questions table to the database schema.

    Args:
        connection: 
            object to use as connection for the application.
    """

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE questions (
            question_id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option_1 TEXT NOT NULL,
            option_2 TEXT NOT NULL,
            option_3 TEXT NOT NULL,
            option_4 TEXT NOT NULL,
            correct_option TEXT NOT NULL
            );
    """)

    connection.commit()


def initialize_database():
    """Initializes the database with connection object."""

    connection = get_database_connection()
    drop_tables(connection)
    create_table_users(connection)
    create_table_questions(connection)
    create_table_user_stats(connection)


if __name__ == "__main__":
    initialize_database()
