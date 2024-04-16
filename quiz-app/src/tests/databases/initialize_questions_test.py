import unittest
from unittest.mock import Mock
from initialize_questions import initialize_questions


class TestInitializeQuestions(unittest.TestCase):
    def setUp(self):
        self.mock_connection = Mock()
        self.mock_quiz_repository = Mock()

    def test_initialize_questions_works(self):
        initialize_questions(self.mock_connection, self.mock_quiz_repository)

        self.mock_quiz_repository.create_question.assert_called()
        self.mock_connection.commit.assert_called_once()

    def test_initialize_questions_with_None_connection(self):
        initialize_questions(
            connection=None, quiz_repository=self.mock_quiz_repository)

        self.mock_quiz_repository.create_question.assert_called()
        self.mock_connection.commit.assert_not_called()

    def test_initialize_questions_with_None_repository(self):
        initialize_questions(
            connection=self.mock_connection, quiz_repository=None)

        self.mock_quiz_repository.create_question.assert_not_called()
        self.mock_connection.commit.assert_called()
