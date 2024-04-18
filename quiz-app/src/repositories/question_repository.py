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
    def __init__(self, connection):
        self._connection = connection

    def create_question(self, quiz) -> object:
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

    def add_points(self, user):
        # this method is used to add points for the user in user_stats table
        pass

    def get_points(self, user):
        # this method should return the points from user_stats table for the given user
        # this is needed for the total points when the quiz ends
        pass


question_repository = QuestionRepository(get_database_connection())
