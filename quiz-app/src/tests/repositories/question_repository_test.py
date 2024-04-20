import unittest
from repositories.question_repository import question_repository
from entities.quiz import Quiz


class TestQuestionRepository(unittest.TestCase):
    def setUp(self):
        question_repository.delete_all()
        self.question = Quiz(1, "What is the capital of Finland?", [
            "Stockholm", "Helsinki", "Oslo", "Copenhagen"], "Helsinki")

    def test_create_new_question_creates_correct_question(self):
        question = question_repository.create_question(self.question)
        all_questions = question_repository.get_all()

        self.assertEqual(len(all_questions), 1)
        self.assertEqual(all_questions[0].question_id, question.question_id)
        self.assertEqual(all_questions[0].question, question.question)
        self.assertEqual(all_questions[0].options, question.options)
        self.assertEqual(
            all_questions[0].correct_option, question.correct_option)
