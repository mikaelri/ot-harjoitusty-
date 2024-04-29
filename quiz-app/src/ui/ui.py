from ui.login_page import LoginPage
from ui.create_user_page import CreateUserPage
from ui.user_page import UserPage
from ui.quiz_page import QuizPage
from ui.highscore_page import HighscorePage


class UI:
    """Class, which is used to handle the user interface."""

    def __init__(self, root):
        """Constructor for UI class, handles the user interface operations.

        Args:
            root: 
                base for tkinter, initializes the app view.
        """

        self._root = root
        self._current_page = None

    def start(self):
        """Starts the user interface"""

        self._show_login_page()

    def _show_login_page(self):
        self._hide_current_page()

        self._current_page = LoginPage(
            self._root,
            self._show_user_page,
            self._show_create_user_page
        )
        self._current_page.pack()

    def _hide_current_page(self):
        if self._current_page:
            self._current_page.destroy()

        self._current_page = None

    def _show_create_user_page(self):
        self._hide_current_page()

        self._current_page = CreateUserPage(
            self._root,
            self._show_user_page,
            self._show_login_page
        )

        self._current_page.pack()

    def _show_user_page(self):
        self._hide_current_page()

        self._current_page = UserPage(
            self._root,
            self._show_start_quiz_page,
            self._show_login_page,
            self._show_highscore_page,
        )
        self._current_page.pack()

    def _show_start_quiz_page(self):
        self._hide_current_page()

        self._current_page = QuizPage(
            self._root,
            self._show_user_page,
        )
        self._current_page.pack()
    
    def _show_highscore_page(self):
        self._hide_current_page()

        self._current_page = HighscorePage(
            self._root,
            self._show_user_page,
        )
        self._current_page.pack()

