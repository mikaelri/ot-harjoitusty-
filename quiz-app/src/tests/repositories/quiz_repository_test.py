import unittest
from repositories.quiz_repository import quiz_repository
from entities.quiz import Quiz


class TestQuizRepository(unittest.TestCase):
    def setUp(self):
        quiz_repository.delete_all()
        self.question = Quiz(1, "What is the capital of Finland?", [
            "Stockholm", "Helsinki", "Oslo", "Copenhagen"
        ], 2)

    def tearDown(self) -> None:
        quiz_repository.delete_all()

    def test_create_new_question_creates_correct_question(self):
        question = quiz_repository.create_question(self.question)
        all_questions = quiz_repository.get_all()

        self.assertEqual(len(all_questions), 1)
        self.assertEqual(all_questions[0].question_id, question.question_id)
        self.assertEqual(all_questions[0].question, question.question)
        self.assertEqual(all_questions[0].options, question.options)
        self.assertEqual(
            all_questions[0].correct_option, question.correct_option)
