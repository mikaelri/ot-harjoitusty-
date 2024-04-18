import random
from entities.quiz import Quiz


from repositories.question_repository import (
    question_repository as default_question_repository
)


class QuestionService:
    def __init__(self, question_repository=default_question_repository):
        self._question_repository = question_repository

    def show_questions(self) -> list:
        questions = self._question_repository.get_all()

        random.shuffle(questions)

        return questions

    def create_question(self, question_id, question, options, correct_option) -> object:
        new_question = Quiz(question_id, question, options, correct_option)

        return self._question_repository.create_question(new_question)

    def check_answer(self, quiz: Quiz, user_answer: int) -> bool:
        # to be updated
        correct_answer = quiz.correct_option
        return correct_answer == user_answer

    def calculate_points(self, user: object):
        # increment points if answer was correct in check_answer() function
        # add_points() in QuestionRepository should increment the points to db so we need to
        # call that function here as well
        # this function might not need to return anything as it just keeps the score
        pass

    def get_points(self, user: object) -> int:
        # this returns the final points when the quiz ends.
        # this calls the get_points() from QuestionRepository
        pass


question_service = QuestionService()
