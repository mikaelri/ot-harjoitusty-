from tkinter import ttk, constants
from services.user_service import user_service


class UserPage:
    def __init__(self, root, handle_start_quiz, handle_logout):

        self._root = root
        self._handle_start_quiz = handle_start_quiz
        self._handle_logout = handle_logout
        self._frame = None
        self._user = user_service.get_current_user()

        self._initialize()

    def pack(self):
        """Showing the view with Tkinter pack-method."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Deletes the current view."""
        self._frame.destroy()

    def _logout_handler(self):
        user_service.logout()
        self._handle_logout()

    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f'Logged in as {self._user.username}')
        user_label.grid(row=0, column=0, padx=5, pady=10, sticky=constants.N)

    def _initialize_info(self):
        info_text = '''
        You will be shown questions with four possible answer options.
        Your task is to try to select the correct answer.

        To start a new quiz, press below - good luck!'''
        quiz_info = ttk.Label(
            master=self._frame,
            text=info_text
        )
        quiz_info.grid(row=1, column=0, padx=5, pady=10, sticky=constants.N)

    def _initialize_new_quiz(self):
        start_quiz_button = ttk.Button(
            master=self._frame,
            style='startquiz.TButton',
            text='Start a new quiz',
            command=self._handle_start_quiz
        )

        style = ttk.Style(self._frame)
        style.configure('startquiz.TButton',
                        foreground='white', background='green', width=30)
        start_quiz_button.grid(row=2, padx=5, pady=10)

    def _initialize_logout(self):
        style = ttk.Style(self._frame)
        style.configure('logout.TButton', foreground='white', background='red')

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            style='logout.TButton',
            command=self._logout_handler
        )
        logout_button.grid(row=0, padx=5, pady=10, sticky=constants.E)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_header()
        self._initialize_info()
        self._initialize_new_quiz()
        self._initialize_logout()
        self._frame.grid_columnconfigure(0, weight=1)
