import random

class Quiz:
    def __init__(self, question_id: int, question: str, options: list, correct_option: str):
        self.question = question
        self.question_id = question_id
        self.options = options
        self.correct_option = correct_option

    def randomize_options(self):
        random.shuffle(self.options)
