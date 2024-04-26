import random
from entities.quiz import Quiz


from repositories.question_repository import (
    question_repository as default_question_repository
)


class QuestionService:
    """Class takin care of the application logic for the quiz."""

    def __init__(self, question_repository=default_question_repository):
        """ Contructor for QuestionService class, handles question and 
        quiz related application logic.

        Args:
            question_repository: 
                By default question_repository.
                Object, which has the methods from QuestionRepository class.  
        """
        self._question_repository = question_repository

    def show_questions(self) -> list:
        """Shows a list of questions in random order

        Returns:
            A list of quiz questions in random order.
        """

        questions = self._question_repository.get_all()

        for question in questions:
            question.randomize_options()

        random.shuffle(questions)

        return questions

    def create_question(self, question_id: int, question: str, options: list, correct_option: str
                        ) -> object:
        """Creates the questions for the quiz.

        Args:
            question_id:
                Integer variable, represents the question id.
            question:
                String variable, represents the question to be added to the quiz.
            options:
                List variable, represents the answer options for the added question.
            correct_option:
                String variable, represents the correct answer for the added question.
        Returns:
            New question as object.
        """

        new_question = Quiz(question_id, question, options, correct_option)

        return self._question_repository.create_question(new_question)

    def check_answer(self, quiz: Quiz, user_answer: str) -> bool:
        """Checks if the user's selected option was correct answer

        Args:
            quiz: 
                Object variable from the Quiz class, data model from entities.
            user_answer:
                String variable of the users selected option.
        Returns:
            boolean value True/False depending if the answer was correct or not.
        """

        correct_answer = quiz.correct_option
        return correct_answer == user_answer

    def calculate_points(self, user: object, quiz: Quiz, user_answer: str) -> int:
        """Adds points for the user if the check_answer returns True, otherwise does nothing.

        Args:
            user:
                Object variable of the user playing the quiz.
            quiz:
                Object variable from the Quiz class, data model from entities.
            user_answer:
                String variable of the users selected option.
        Returns:
            Calculated (increased or not) for the user object.
        """

        user_points = self._question_repository.get_points(user.username)
        correct_answer = self.check_answer(quiz, user_answer)

        if correct_answer:
            self._question_repository.add_points(user.username)
            user_points += 1

        return user_points

    def get_points(self, user: object) -> int:
        """Gets the points for user object.

        Args:
            user:
                Object variable of the user playing the quiz.
        Returns:
            Points for the user object.
        """

        return self._question_repository.get_points(user.username)

    def initialize_points(self, username: str) -> int:
        """Initializes the quiz points to 0 when user starts a new quiz.

        Args:
            username:
                String variable, represents the username of the current user.
        Returns:
            Initialized points to 0 for the username.
        """

        return self._question_repository.initialize_points(username)


question_service = QuestionService()
