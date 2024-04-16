import random
from entities.quiz import Quiz


from repositories.question_repository import (
    question_repository as default_question_repository
)


class QuestionService:
    def __init__(self, question_repository=default_question_repository):
        self._question_repository = question_repository

    # def check_answer(self, quiz: Quiz, user_choice: int) -> bool:
    #     correct_answer = quiz.correct_option
    #     return correct_answer == user_choice

    def show_questions(self) -> list:
        questions = self._question_repository.get_all()

        random.shuffle(questions)

        return questions

    def create_question(self, question_id, question, options, correct_option) -> object:
        new_question = Quiz(question_id, question, options, correct_option)

        return self._question_repository.create_question(new_question)


question_service = QuestionService()
