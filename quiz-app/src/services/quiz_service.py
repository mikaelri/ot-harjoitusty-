from entities.quiz import Quiz

from repositories.quiz_repository import (
    quiz_repository as default_quiz_repository
)


class QuestionService:
    def __init__(self, quiz_repository=default_quiz_repository):
        self._quiz_repository = quiz_repository

    def check_answer(self, quiz: Quiz, user_choice: str) -> bool:
        correct_answer = quiz.options[quiz.correct_option - 1].lower()
        return correct_answer == user_choice.lower()
