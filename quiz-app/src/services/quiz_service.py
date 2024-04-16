import random
from entities.quiz import Quiz


from repositories.quiz_repository import (
    quiz_repository as default_quiz_repository
)


class QuestionService:
    def __init__(self, quiz_repository=default_quiz_repository):
        self._quiz_repository = quiz_repository

    # def check_answer(self, quiz: Quiz, user_choice: int) -> bool:
    #     correct_answer = quiz.correct_option
    #     return correct_answer == user_choice

    def show_questions(self):
        questions = self._quiz_repository.get_all()

        random.shuffle(questions)

        return questions

    def create_question(self, question_id, question, options, correct_option):
        new_question = Quiz(question_id, question, options, correct_option)

        return self._quiz_repository.create_question(new_question)


quiz_service = QuestionService()
