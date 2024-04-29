import unittest
from repositories.question_repository import question_repository
from repositories.user_repository import user_repository
from entities.quiz import Quiz
from entities.user import User, UserStats


class TestQuestionRepository(unittest.TestCase):
    def setUp(self):
        question_repository.delete_all()
        user_repository.delete_all()
        question_repository.delete_all_user_points()

        self.question = Quiz(1, "What is the capital of Finland?", [
            "Stockholm", "Helsinki", "Oslo", "Copenhagen"], "Helsinki")
        self.user_player1 = User("player1", "player1password")
        self.user_player1_points = UserStats(self.user_player1.username, 0)

        self.user_player2 = User("player2", "player2password")
        self.user_player2_points = UserStats(self.user_player2.username, 0)

        self.user_player3 = User("player3", "player3password")
        self.user_player3_points = UserStats(self.user_player3.username, 0)

        self.user_player4 = User("player4", "player4password")
        self.user_player4_points = UserStats(self.user_player4.username, 0)

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

    def test_get_highscore_for_user(self):
        user = self.create_user(self.user_player1)

        question_repository.add_points(user.username)
        question_repository.add_points(user.username)
        user_points = question_repository.get_points(user.username)

        question_repository.update_highscore(user.username)
        user_highscore = question_repository.get_highscore(user.username)

        self.assertEqual(user_points, user_highscore)

    def test_get_top_highscores_for_top_3_users(self):
        user1 = self.create_user(self.user_player1)
        user2 = self.create_user(self.user_player2)
        user3 = self.create_user(self.user_player3)

        question_repository.add_points(user1.username)
        question_repository.add_points(user1.username)
        question_repository.add_points(user1.username)
        question_repository.add_points(user1.username)
        question_repository.update_highscore(user1.username)
        user1_highscore = question_repository.get_highscore(user1.username)

        question_repository.add_points(user2.username)
        question_repository.add_points(user2.username)
        question_repository.add_points(user2.username)
        question_repository.update_highscore(user2.username)
        user2_highscore = question_repository.get_highscore(user2.username)

        question_repository.add_points(user3.username)
        question_repository.update_highscore(user3.username)
        user3_highscore = question_repository.get_highscore(user3.username)

        highscore_list = question_repository.get_top_highscores()

        self.assertEqual(highscore_list[0][1], user1_highscore)
        self.assertEqual(highscore_list[1][1], user2_highscore)
        self.assertEqual(highscore_list[2][1], user3_highscore)

    def test_get_top_highscores_for_top_3_users_if_less_than_3_users(self):
        user1 = self.create_user(self.user_player1)
        user2 = self.create_user(self.user_player2)

        question_repository.add_points(user1.username)
        question_repository.update_highscore(user1.username)
        user1_highscore = question_repository.get_highscore(user1.username)

        question_repository.add_points(user2.username)
        question_repository.add_points(user2.username)
        question_repository.update_highscore(user2.username)
        user2_highscore = question_repository.get_highscore(user2.username)

        highscore_list = question_repository.get_top_highscores()

        self.assertEqual(highscore_list[0][1], user2_highscore)
        self.assertEqual(highscore_list[1][1], user1_highscore)
        self.assertEqual(len(highscore_list), 2)

    def test_get_top_highscores_for_top_3_users_if_more_than_3_users(self):
        user1 = self.create_user(self.user_player1)
        user2 = self.create_user(self.user_player2)
        user3 = self.create_user(self.user_player3)
        user4 = self.create_user(self.user_player4)

        question_repository.add_points(user1.username)
        question_repository.add_points(user1.username)
        question_repository.add_points(user1.username)
        question_repository.add_points(user1.username)
        question_repository.update_highscore(user1.username)
        user1_highscore = question_repository.get_highscore(user1.username)

        question_repository.add_points(user2.username)
        question_repository.add_points(user2.username)
        question_repository.add_points(user2.username)
        question_repository.update_highscore(user2.username)
        user2_highscore = question_repository.get_highscore(user2.username)

        question_repository.add_points(user3.username)
        question_repository.add_points(user3.username)
        question_repository.update_highscore(user3.username)
        user3_highscore = question_repository.get_highscore(user3.username)

        question_repository.add_points(user4.username)
        question_repository.update_highscore(user4.username)
        user4_highscore = question_repository.get_highscore(user4.username)

        highscore_list = question_repository.get_top_highscores()

        self.assertEqual(highscore_list[0][1], user1_highscore)
        self.assertEqual(highscore_list[1][1], user2_highscore)
        self.assertEqual(highscore_list[2][1], user3_highscore)

        top_highscores = [points[1] for points in highscore_list]

        self.assertNotIn(user4_highscore, top_highscores)
