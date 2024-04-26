import random


class Quiz:
    """Clas for the questions.

    Attributes:
        question_id:
            Questions identifier as integer.
        question:
            Question as a string variable.
        options:
            Options for the question's answer as a list.
        correct_option:
            Questions correct answer as string variable.
    """

    def __init__(self, question_id: int, question: str, options: list, correct_option: str):
        """Constructor for the class, data model of the Quiz object.

        Args:
            question_id:
                Questions identifier as integer.
            question:
                Question as a string variable.
            options:
                Options for the question's answer as a list.
            correct_option:
                Questions correct answer as string variable.
        """

        self.question_id = question_id
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def randomize_options(self) -> None:
        """Puts the options in a random order."""

        random.shuffle(self.options)
