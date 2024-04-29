from database_connection import get_database_connection
from entities.quiz import Quiz


def get_question_by_row(row: any) -> object:
    """Gets the questions in a row, used in mapping all of the questions to a list.

    Args:
        row:
            Selected variable for the questions table
    Returns:
        A question object in a row, formed in Quiz model from entities or None.
    """

    return Quiz(
        row['question_id'],
        row['question'],
        [row['option_1'], row['option_2'], row['option_3'], row['option_4']],
        row['correct_option']
    ) if row else None


class QuestionRepository:
    """Class taking care of the quiz related database operations."""

    def __init__(self, connection: object):
        """Constructor for QuestionRepository class, handles the quiz database changes for th user
        and questions.

        Args:
            connection: Database object for the connection.
        """

        self._connection = connection

    def create_question(self, quiz: object) -> object:
        """Creates the question to the database.

        Args:
            quiz:
                A question to be saved to the database as object.
        Returns:
            Saved question as object.
        """

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
        """Gets all questions from the database.

        Returns:
            A list of all questions.
        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM questions")
        rows = cursor.fetchall()

        return list(map(get_question_by_row, rows))

    def delete_all(self) -> None:
        """Deletes all of the questions from the database."""

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM questions")
        self._connection.commit()

    def delete_all_user_points(self) -> None:
        """Deletes all of the user points from the database."""

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM user_stats")
        self._connection.commit()

    def get_points(self, username: str) -> int:
        """Get the quiz points from the database for the current user playing.

        Args:
            username:
                String variable, represents the username for the user object.
        Returns:
            The quiz points of the username for the user object or 0.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT quiz_points FROM user_stats WHERE username = ?", (username,))
        row = cursor.fetchone()

        return row[0] if row else 0

    def add_points(self, username: str) -> None:
        """Adds points to the database for the current user playing the quiz.

        Args:
            username:
                String variable, represents the username for the user object.
        """

        cursor = self._connection.cursor()
        cursor.execute("""UPDATE user_stats SET quiz_points = quiz_points +1 WHERE username = ?""",
                       (username,))
        self._connection.commit()

    def initialize_points(self, username: str) -> None:
        """Initializes the points to 0 in the database for the current user playing the quiz.

        Args:
            username:
                String variable, represents the username for the user object.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE user_stats SET quiz_points = 0 WHERE username = ?", (username,))
        self._connection.commit()

    def get_highscore(self, username: str) -> int:
        """Get the highscore from the database for the current user playing.

        Args:
            username:
                String variable, represents the username for the user object.
        Returns:
            The highscore of the username for the user object as integer or 0.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT highscore FROM user_stats WHERE username = ?", (username,))
        row = cursor.fetchone()

        return row[0] if row else 0

    def update_highscore(self, username: str) -> None:
        """Updates the highscore for the user if current quiz_points are higher
        than previous highscore for the user.

        Args:
            username:
                String variable, represents the username for the user object.
        """
        cursor = self._connection.cursor()
        cursor.execute("""UPDATE user_stats SET highscore = quiz_points WHERE username = ?""",
                       (username,))
        self._connection.commit()

    def get_top_highscores(self) -> list:
        """Get the top 3 highscores from the database for the users.

        Returns:
            A list of tuples for users, for the top 3 (or less) users with most quiz points
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT username, highscore FROM user_stats ORDER BY highscore DESC LIMIT 3")
        rows = cursor.fetchall()

        return rows


question_repository = QuestionRepository(get_database_connection())
