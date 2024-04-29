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
        self.highscore = 0
        self.user_scores = {}

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

    def get_highscore(self, username):
        return self.highscore

    def update_highscore(self, username):
        self.highscore = self.user_points
        return self.highscore

    def get_top_highscores(self):
        return sorted(self.user_scores.items(), key=lambda item: item[1], reverse=True)[:3]


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

        self.question_id = self.question_package.question_id
        self.question = self.question_package.question
        self.options = self.question_package.options
        self.correct_option = self.question_package.correct_option

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
        self.create_questions(self.question_id, self.question,
                              self.options, self.correct_option)
        all_questions = self.get_questions()

        all_options = {"Stockholm", "Helsinki", "Oslo", "Copenhagen"}

        self.assertEqual(len(all_questions), 1)
        self.assertEqual(all_questions[0].question_id, 1)
        self.assertEqual(all_questions[0].question,
                         "What is the capital of Finland?")
        self.assertEqual(set(all_questions[0].options), all_options)
        self.assertEqual(all_questions[0].correct_option, "Helsinki")

    def test_check_correct_answer_returns_True_and_points_are_increased(self):
        self.create_questions(self.question_id, self.question,
                              self.options, self.correct_option)

        all_questions = self.get_questions()
        quiz_question = all_questions[0]
        user_answer = "Helsinki"

        result = self.check_answer(quiz_question, user_answer)
        self.assertTrue(result)

        user_points = self.question_service.calculate_points(
            self.user_player1, quiz_question, user_answer)
        self.assertEqual(user_points, 1)

    def test_check_wrong_answer_returns_False_and_points_are_not_increased(self):
        self.create_questions(self.question_id, self.question,
                              self.options, self.correct_option)

        all_questions = self.get_questions()
        quiz_question = all_questions[0]
        user_answer = "Copenhagen"

        result = self.check_answer(quiz_question, user_answer)
        self.assertFalse(result)

        user_points = self.question_service.calculate_points(
            self.user_player1, quiz_question, user_answer)
        self.assertEqual(user_points, 0)

    def test_get_points_returns_correct_points_and_initialize_point_sets_points_to_zero(self):
        self.create_questions(self.question_id, self.question,
                              self.options, self.correct_option)

        all_questions = self.get_questions()
        quiz_question = all_questions[0]
        user_answer = "Helsinki"

        get_initial_points = self.question_service.get_points(
            self.user_player1)
        self.assertEqual(get_initial_points, 0)

        self.check_answer(quiz_question, user_answer)
        self.question_service.calculate_points(
            self.user_player1, quiz_question, user_answer)

        get_points = self.question_service.get_points(self.user_player1)
        self.assertEqual(get_points, 1)

        self.question_service.initialize_points(self.user_player1.username)
        get_initialized_points = self.question_service.get_points(
            self.user_player1)
        self.assertEqual(get_initialized_points, 0)

    def test_highscore_is_updated_correctly_if_user_answers_correctly_and_has_points(self):
        self.create_questions(self.question_id, self.question,
                              self.options, self.correct_option)

        all_questions = self.get_questions()
        quiz_question = all_questions[0]
        user_answer = "Helsinki"

        user_points = self.question_service.calculate_points(
            self.user_player1, quiz_question, user_answer)

        updated_user_highscore = self.question_service.update_highscore(
            self.user_player1)

        self.assertEqual(user_points, updated_user_highscore)

    def test_highscore_is_updated_correctly_if_user_has_no_points(self):
        self.create_questions(self.question_id, self.question,
                              self.options, self.correct_option)

        user_points = self.question_service.get_points(self.user_player1)
        updated_user_highscore = self.question_service.update_highscore(
            self.user_player1)

        self.assertEqual(user_points, updated_user_highscore)

    def test_highscore_is_displayed_correctly_for_user_when_user_has_no_points(self):

        user_points = self.question_service.get_points(self.user_player1)
        self.question_service.update_highscore(self.user_player1)
        get_user_highscore = self.question_service.get_highscore(
            self.user_player1)

        self.assertEqual(user_points, get_user_highscore)

    def test_highscore_is_displayed_correctly_for_user_when_user_has_points(self):
        self.create_questions(self.question_id, self.question,
                              self.options, self.correct_option)

        all_questions = self.get_questions()
        quiz_question = all_questions[0]
        user_answer = "Helsinki"

        user_points = self.question_service.calculate_points(
            self.user_player1, quiz_question, user_answer)

        user_points = self.question_service.get_points(self.user_player1)
        self.question_service.update_highscore(self.user_player1)
        get_user_highscore = self.question_service.get_highscore(
            self.user_player1)

        self.assertEqual(user_points, get_user_highscore)

    def test_top_3_highscores_are_displayed_correctly(self):
        users = [
            User('player1', 'player1password'),
            User('player2', 'player2password'),
            User('player3', 'player3password'),
            User('player4', 'player4password')
        ]

        user_stats = [4, 3, 2, 1]

        for user, points in zip(users, user_stats):
            self.question_service._question_repository.user_scores[user.username] = points
            self.question_service.update_highscore(user)

        expected_highscores = [
            ('player1', 4),
            ('player2', 3),
            ('player3', 2)
        ]

        highscores = self.question_service.get_top_highscores()

        self.assertEqual(highscores, expected_highscores)
