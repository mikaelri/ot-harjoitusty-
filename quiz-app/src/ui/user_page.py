from tkinter import ttk, constants
from services.user_service import user_service
from services.question_service import question_service


class UserPage:
    """Class, which is used for user operations and starting a new quiz."""

    def __init__(self, root, handle_start_quiz, handle_logout, handle_highscore):
        """Constructor for UserPage class, handles starting a new quiz and logout.

        Args:
            root: 
                Base for tkinter, initializes the app view.
            handle_start_quiz: 
                Called variable to move to new quiz view.
            handle_logout: 
                Called variable to logout and move to front page.
        """

        self._root = root
        self._handle_start_quiz = handle_start_quiz
        self._handle_logout = handle_logout
        self._handle_highscore = handle_highscore
        self._frame = None
        self._user = user_service.get_current_user()
        self._questions = question_service.show_questions()

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
        info_text = f'''
        You will be shown {len(self._questions)} questions with four possible answer options each.

                        Your task is to try to select the correct answer.
                        
                                Your current highscore is: {
                                question_service.get_highscore(self._user)}/{
                                    len(self._questions)} points.

                        To start a new quiz, press below - good luck!'''

        quiz_info = ttk.Label(
            master=self._frame,
            text=info_text
        )
        quiz_info.grid(row=1, column=0, padx=5, pady=10, sticky=constants.N)

    def _start_new_quiz(self):
        question_service.initialize_points(self._user.username)
        self._handle_start_quiz()

    def _initialize_new_quiz(self):
        start_quiz_button = ttk.Button(
            master=self._frame,
            style='startquiz.TButton',
            text='Start a new quiz',
            command=self._start_new_quiz
        )

        style = ttk.Style(self._frame)
        style.configure('startquiz.TButton',
                        foreground='white', background='green', width=30)
        start_quiz_button.grid(row=2, padx=5, pady=10)

    def _initialize_highscore(self):
        highscore_button = ttk.Button(
            master=self._frame,
            style='highscore.TButton',
            text='Show top 3 highscores',
            command=self._handle_highscore
        )

        style = ttk.Style(self._frame)
        style.configure('highscore.TButton',
                        foreground='white', background='grey', width=30)
        highscore_button.grid(row=3, padx=5, pady=10)

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
        self._initialize_highscore()
        self._initialize_logout()
        self._frame.grid_columnconfigure(0, weight=1)
