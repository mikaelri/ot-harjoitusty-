from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("DROP TABLE if exists users;")
    cursor.execute("DROP TABLE if exists questions;")

    connection.commit()

def create_table_users(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE users (
            username TEXT PRIMARY KEY,
            password TEXT
            );
    """)
    
    connection.commit()

def create_table_questions(connection):
    pass 

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_table_users(connection)
    create_table_questions(connection)

if __name__ == "__main__":
    initialize_database()
    