class Quiz:
    def __init__(self, question_id: int, question: str, options: list, correct_option: int):
        self.question = question
        self.question_id = question_id
        self.options = options
        self.correct_option = correct_option
