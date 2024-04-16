from tkinter import ttk, constants
from services.question_service import question_service
from services.user_service import user_service


class QuizPage:
    def __init__(self, root, handle_user_page):

        self._root = root
        self._handle_user_page = handle_user_page
        self._frame = None
        self._user = user_service.get_current_user()
        self._questions = []
        self._current_question_index = 0
        self._current_question = None

        self._initialize()

    def pack(self):
        """Showing the view with Tkinter pack-method."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Deletes the current view."""
        self._frame.destroy()

    def _show_quiz_questions(self):
        self.questions = question_service.show_questions()
        self._current_question_index = 0
        self.current_question = self.questions[self._current_question_index]
        question_index = 1

        for question in self.questions:
            question_label = ttk.Label(self._frame, text=question.question)
            question_label.grid(row=question_index + 1,
                                column=0, sticky=constants.W, padx=10, pady=5)

            for idx, option in enumerate(question.options):
                option_button = ttk.Button(
                    self._frame, text=option, command=lambda idx=idx: self._handle_option(idx))
                option_button.grid(
                    row=question_index + 2, column=idx, sticky=constants.W, padx=10, pady=2)

            question_index += 2

    def _handle_option(self, option_index):
        selected_answer = option_index + 1
        current_question = self.current_question
        correct_answer = current_question.correct_option

        if selected_answer == correct_answer:
            pass
            ### own notes, to be deleted ###
            ### collect points from correct answers, 1 pts###
            ### create a function so that the self._user will gather points with correct answers##
        else:
            ### 0 pts for wrong answer###
            pass

        if self.current_question_index < len(self.questions):
            self.current_question = self.questions[self.current_question_index + 1]
            self._show_quiz_questions()
        else:
            ### quiz will end and the final results will be shown when there is no more questions###
            ### create a function so that the self._user points will be shown here ###
            ### add a end quiz button, which will direct the user to the user page ###
            pass

    def _initialize_header(self):
        quiz_label = ttk.Label(
            master=self._frame, text=f'Playing as {self._user.username}')
        quiz_label.grid(row=0, column=0, padx=5, pady=10, sticky=constants.N,)

    def _initialize_user_page(self):
        user_page_button = ttk.Button(
            master=self._frame,
            text="End quiz & return to user page",
            command=self._handle_user_page
        )
        user_page_button.grid(row=0, padx=5, pady=10, sticky=constants.E)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_header()
        self._initialize_user_page()
        self._show_quiz_questions()
        self._frame.grid_columnconfigure(0, weight=1)
