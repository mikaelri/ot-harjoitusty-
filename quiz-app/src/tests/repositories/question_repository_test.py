import unittest
from repositories.question_repository import question_repository
from repositories.user_repository import user_repository
from entities.quiz import Quiz
from entities.user import User, UserStats


class TestQuestionRepository(unittest.TestCase):
    def setUp(self):
        question_repository.delete_all()
        user_repository.delete_all()
        self.question = Quiz(1, "What is the capital of Finland?", [
            "Stockholm", "Helsinki", "Oslo", "Copenhagen"], "Helsinki")
        self.user_player1 = User("player1", "player1password")
        self.user_player1_points = UserStats(self.user_player1.username, 0)
        question_repository.delete_all_user_points()

    def create_user(self, user):
        return user_repository.create_user(user)

    def test_create_new_question_creates_correct_question(self):
        question = question_repository.create_question(self.question)
        all_questions = question_repository.get_all()

        self.assertEqual(len(all_questions), 1)
        self.assertEqual(all_questions[0].question_id, question.question_id)
        self.assertEqual(all_questions[0].question, question.question)
        self.assertEqual(all_questions[0].options, question.options)
        self.assertEqual(
            all_questions[0].correct_option, question.correct_option)

    def test_get_points_for_user(self):
        user = self.create_user(self.user_player1)
        user_points = question_repository.get_points(user.username)

        self.assertEqual(user_points, 0)

    def test_add_one_point_for_user(self):
        user = self.create_user(self.user_player1)

        question_repository.add_points(user.username)
        user_points = question_repository.get_points(user.username)

        self.assertEqual(user_points, 1)

    def test_add_several_points_for_user(self):
        user = self.create_user(self.user_player1)

        question_repository.add_points(user.username)
        question_repository.add_points(user.username)
        question_repository.add_points(user.username)
        user_points = question_repository.get_points(user.username)

        self.assertEqual(user_points, 3)

    def test_initialize_points_for_new_quiz(self):
        user = self.create_user(self.user_player1)

        question_repository.add_points(user.username)
        question_repository.add_points(user.username)
        question_repository.add_points(user.username)

        question_repository.initialize_points(user.username)
        user_points = question_repository.get_points(user.username)

        self.assertEqual(user_points, 0)
