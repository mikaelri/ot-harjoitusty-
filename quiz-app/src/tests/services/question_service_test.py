import unittest
from entities.quiz import Quiz
from entities.user import User, UserStats
from services.user_service import UserService
from services.question_service import QuestionService
from tests.services.user_service_test import FakeUserRepository


class FakeQuestionRepository:
    def __init__(self, questions=[]):
        self.questions = questions if questions is not None else []
        self.user_points = 0

    def get_all(self):
        return self.questions

    def get_points(self, username):
        return self.user_points

    def add_points(self, username):
        self.user_points += 1

    def initialize_points(self, username):
        self.user_points = 0

    def create_question(self, question):
        self.questions.append(question)

    def delete_all_questions(self):
        self.questions = []

    def delete_all_points(self):
        self.user_points = 0


class TestQuestionService(unittest.TestCase):
    def setUp(self):

        fake_user_repository = FakeUserRepository()
        self.user_service = UserService(fake_user_repository)

        fake_user_repository.delete_all()
        self.user_player1 = User("player1", "player1password")
        self.user_player1_points = UserStats(self.user_player1.username, 0)

        fake_question_repository = FakeQuestionRepository()
        self.question_service = QuestionService(fake_question_repository)
        fake_question_repository.delete_all_questions()
        fake_question_repository.delete_all_points()

        self.question_package = Quiz(1, "What is the capital of Finland?", [
            "Stockholm", "Helsinki", "Oslo", "Copenhagen"
        ], "Helsinki")

    def create_questions(self, question_id, question, options, correct_option):
        self.question_service.create_question(
            question_id, question, options, correct_option)

    def get_questions(self):
        return self.question_service.show_questions()

    def check_answer(self, quiz, user_answer):
        return self.question_service.check_answer(quiz, user_answer)

    def create_new_user(self, username, password, password2):
        return self.user_service.create_user(username, password, password2)

    def login_user(self, username, password):
        return self.user_service.login(username, password)

    def test_questions_are_shown_correctly(self):
        question_id = self.question_package.question_id
        question = self.question_package.question
        options = self.question_package.options
        correct_option = self.question_package.correct_option

        self.create_questions(question_id, question, options, correct_option)
        all_questions = self.get_questions()

        self.assertEqual(len(all_questions), 1)
        self.assertEqual(all_questions[0].question_id, 1)
        self.assertEqual(all_questions[0].question,
                         "What is the capital of Finland?")
        self.assertEqual(all_questions[0].options, [
                         "Stockholm", "Helsinki", "Oslo", "Copenhagen"])
        self.assertEqual(all_questions[0].correct_option, "Helsinki")

    def test_check_correct_answer_returns_True_and_points_are_increased(self):
        question_id = self.question_package.question_id
        question = self.question_package.question
        options = self.question_package.options
        correct_option = self.question_package.correct_option
        self.create_questions(question_id, question, options, correct_option)

        all_questions = self.get_questions()
        quiz_question = all_questions[0]
        user_answer = "Helsinki"

        result = self.check_answer(quiz_question, user_answer)
        self.assertTrue(result)

        user_points = self.question_service.calculate_points(
            self.user_player1, quiz_question, user_answer)
        self.assertEqual(user_points, 1)

    def test_check_wrong_answer_returns_False_and_points_are_not_increased(self):
        question_id = self.question_package.question_id
        question = self.question_package.question
        options = self.question_package.options
        correct_option = self.question_package.correct_option
        self.create_questions(question_id, question, options, correct_option)

        all_questions = self.get_questions()
        quiz_question = all_questions[0]
        user_answer = "Copenhagen"

        result = self.check_answer(quiz_question, user_answer)
        self.assertFalse(result)

        user_points = self.question_service.calculate_points(
            self.user_player1, quiz_question, user_answer)
        self.assertEqual(user_points, 0)

    def test_get_points_returns_correct_points_and_initialize_point_sets_points_to_zero(self):
        question_id = self.question_package.question_id
        question = self.question_package.question
        options = self.question_package.options
        correct_option = self.question_package.correct_option
        self.create_questions(question_id, question, options, correct_option)

        all_questions = self.get_questions()
        quiz_question = all_questions[0]
        user_answer = "Helsinki"

        self.check_answer(quiz_question, user_answer)
        self.question_service.calculate_points(
            self.user_player1, quiz_question, user_answer)

        get_points = self.question_service.get_points(self.user_player1)
        self.assertEqual(get_points, 1)

        self.question_service.initialize_points(self.user_player1.username)
        get_initialized_points = self.question_service.get_points(
            self.user_player1)
        self.assertEqual(get_initialized_points, 0)
