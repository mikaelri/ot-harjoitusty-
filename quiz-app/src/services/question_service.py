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

        for question in questions:
            question.randomize_options()
            
        random.shuffle(questions)

        return questions

    def create_question(self, question_id, question, options, correct_option) -> object:
        new_question = Quiz(question_id, question, options, correct_option)

        return self._question_repository.create_question(new_question)

    def check_answer(self, quiz: Quiz, user_answer: str) -> bool:
        correct_answer = quiz.correct_option
        return correct_answer == user_answer

    def calculate_points(self, user: object, quiz: Quiz, user_answer: int) -> int:
        user_points = self._question_repository.get_points(user.username)
        correct_answer = self.check_answer(quiz, user_answer)

        if correct_answer:
            self._question_repository.add_points(user.username)
            user_points += 1

        return user_points

    def get_points(self, user: object) -> int:
        return self._question_repository.get_points(user.username)

    def initialize_points(self, username: str) -> int:
        return self._question_repository.initialize_points(username)


question_service = QuestionService()
