import unittest
from entities.quiz import Quiz
from services.quiz_service import QuestionService


class FakeQuizRepository:
    def __init__(self, questions=[]):
        self.questions = questions if questions is not None else []

    def get_all(self):
        return self.questions

    def create_question(self, question):
        self.questions.append(question)

    def delete_all(self):
        self.questions = []


class TestQuestionService(unittest.TestCase):
    def setUp(self):
        fake_quiz_repository = FakeQuizRepository()
        self.quiz_service = QuestionService(fake_quiz_repository)

        fake_quiz_repository.delete_all()

        self.question_package = Quiz(1, "What is the capital of Finland?", [
            "Stockholm", "Helsinki", "Oslo", "Copenhagen"
        ], 2)

    def test_questions_are_shown_correctly(self):
        question_id = self.question_package.question_id
        question = self.question_package.question
        options = self.question_package.options
        correct_option = self.question_package.correct_option

        self.quiz_service.create_question(
            question_id, question, options, correct_option)

        all_questions = self.quiz_service.show_questions()

        self.assertEqual(len(all_questions), 1)
        self.assertEqual(all_questions[0].question_id, 1)
        self.assertEqual(all_questions[0].question,
                         "What is the capital of Finland?")
        self.assertEqual(all_questions[0].options, [
                         "Stockholm", "Helsinki", "Oslo", "Copenhagen"])
        self.assertEqual(all_questions[0].correct_option, 2)
