from ui.login_page import LoginPage
from ui.create_user_page import CreateUserPage

class UI:
    def __init__(self, root):
        self._root = root
        self._current_page = None

    def start(self):
        self._show_login_page()

    def _show_login_page(self):
        self._hide_current_page()

        self._current_page = LoginPage(
            self._root,
            self._show_login_page,
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
            self._show_login_page
        )

        self._current_view.pack()
