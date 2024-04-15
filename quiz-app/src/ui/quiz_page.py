from tkinter import ttk, constants
from services.quiz_service import quiz_service
from services.user_service import user_service


class QuizPage:
    def __init__(self, root, handle_user_page):

        self._root = root
        self._handle_user_page = handle_user_page
        self._frame = None
        self._user = user_service.get_current_user()

        self._initialize()

    def pack(self):
        """Showing the view with Tkinter pack-method."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Deletes the current view."""
        self._frame.destroy()

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

    def _show_quiz_guestions(self):
        pass
        # update to show the questions

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_header()
        self._initialize_user_page()
        self._show_quiz_guestions()
        self._frame.grid_columnconfigure(0, weight=1)
