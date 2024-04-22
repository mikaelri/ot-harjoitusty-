from database_connection import get_database_connection
from entities.quiz import Quiz


def get_question_by_row(row) -> object:
    return Quiz(
        row['question_id'],
        row['question'],
        [row['option_1'], row['option_2'], row['option_3'], row['option_4']],
        row['correct_option']
    ) if row else None


class QuestionRepository:
    def __init__(self, connection: str):
        self._connection = connection

    def create_question(self, quiz: object) -> object:
        cursor = self._connection.cursor()
        cursor.execute(
            """INSERT INTO questions 
            (question, option_1, option_2, option_3, option_4, correct_option) 
            VALUES (?, ?, ?, ?, ?, ?)""",
            (quiz.question, quiz.options[0], quiz.options[1],
             quiz.options[2], quiz.options[3], quiz.correct_option)
        )
        self._connection.commit()

        return quiz

    def get_all(self) -> list:
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM questions")
        rows = cursor.fetchall()

        return list(map(get_question_by_row, rows))

    def delete_all(self) -> None:
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM questions")
        self._connection.commit()

    def delete_all_user_points(self) -> None:
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM user_stats")
        self._connection.commit()

    def get_points(self, username: str) -> int:
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT quiz_points FROM user_stats WHERE username = ?", (username,))
        row = cursor.fetchone()

        return row[0] if row else 0

    def add_points(self, username: str):
        cursor = self._connection.cursor()
        cursor.execute("""UPDATE user_stats SET quiz_points = quiz_points +1 WHERE username = ?""",
                       (username,))
        self._connection.commit()

    def initialize_points(self, username: str):
        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE user_stats SET quiz_points = 0 WHERE username = ?", (username,))
        self._connection.commit()


question_repository = QuestionRepository(get_database_connection())
