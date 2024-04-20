import unittest
from entities.quiz import Quiz
from services.question_service import QuestionService


class FakeQuestionRepository:
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
        fake_question_repository = FakeQuestionRepository()
        self.question_service = QuestionService(fake_question_repository)

        fake_question_repository.delete_all()

        self.question_package = Quiz(1, "What is the capital of Finland?", [
            "Stockholm", "Helsinki", "Oslo", "Copenhagen"
        ], "Helsinki")

    def test_questions_are_shown_correctly(self):
        question_id = self.question_package.question_id
        question = self.question_package.question
        options = self.question_package.options
        correct_option = self.question_package.correct_option

        self.question_service.create_question(
            question_id, question, options, correct_option)

        all_questions = self.question_service.show_questions()

        self.assertEqual(len(all_questions), 1)
        self.assertEqual(all_questions[0].question_id, 1)
        self.assertEqual(all_questions[0].question,
                         "What is the capital of Finland?")
        self.assertEqual(all_questions[0].options, [
                         "Stockholm", "Helsinki", "Oslo", "Copenhagen"])
        self.assertEqual(all_questions[0].correct_option, "Helsinki")
