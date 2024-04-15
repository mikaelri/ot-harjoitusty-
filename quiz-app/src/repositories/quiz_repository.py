from database_connection import get_database_connection


class QuizRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_question(self, quiz):
        cursor = self._connection.cursor()
        cursor.execute(
            """INSERT INTO questions 
            (question, option_1, option_2, option_3, option_4, correct_option) 
            VALUES (?, ?, ?, ?, ?, ?)""",
            (quiz.question, quiz.options[0], quiz.options[1],
             quiz.options[2], quiz.options[3], quiz.correct_option)
        )
        self._connection.commit()

        return cursor.lastrowid


quiz_repository = QuizRepository(get_database_connection())