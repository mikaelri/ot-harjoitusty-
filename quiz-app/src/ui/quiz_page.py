from tkinter import ttk, constants
from services.question_service import question_service
from services.user_service import user_service


class QuizPage:
    def __init__(self, root, handle_user_page):

        self._root = root
        self._handle_user_page = handle_user_page
        self._frame = None
        self._user = user_service.get_current_user()
        self._questions = question_service.show_questions()
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
        # update that the buttons are set in a way that?:
        # option option
        # option option
        if self._current_question:
            self._current_question.grid_forget()        

        if self._current_question_index < len(self._questions):
            current_question = self._questions[self._current_question_index]
            question_label = ttk.Label(
                master=self._frame,
                text=current_question.question
            )
            question_label.grid(row=1, column=0, padx=5, pady=10, sticky="N")
            self._current_question = question_label

            for i, option in enumerate(current_question.options):
                option_button = ttk.Button(
                    master=self._frame,
                    text=option,
                    command=lambda idx=i, question=current_question: self._handle_option(
                        question, idx)
                )
                option_button.grid(row=i+2, column=0, padx=5,
                                   pady=5, sticky=constants.N)

    def _handle_option(self, question, option_index):
        selected_option = question.options[option_index]
        is_correct = question_service.check_answer(question, selected_option)

        if is_correct:
            question_service.calculate_points(
                self._user, question, selected_option)

        self._current_question_index += 1

        if self._current_question_index < len(self._questions):
            self._show_quiz_questions()
            ### add that ending quiz while still playing puts the user points to zero ###
            ### if the user plays all the questions, then no need to update points to zero ###
            ### as starting new quiz will initialize the user_points already ###
            # for keeping up the highscore of the user, must add possibly the following:
            # - user_stats db a new column "highscore"
            # - logic that the highscore is replaced with quiz_points if quiz_points > highscore
            # - highscore will be kept for the user and not initialized, initialize only quiz_points
        else:
            self._end_quiz()

    def _end_quiz(self):
        total_points = question_service.get_points(self._user)
        ttk.Label(
            master=self._frame,
            text=f"Quiz ended. You scored {total_points} points."
        ).grid(row=self._current_question_index + 2, column=0, padx=5, pady=10, sticky=constants.W)

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
