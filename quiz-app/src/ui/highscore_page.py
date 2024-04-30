from tkinter import ttk, constants
from services.user_service import user_service
from services.question_service import question_service


class HighscorePage:
    """Class, which is used for showing highscores"""

    def __init__(self, root, handle_user_page):
        """Constructor for HighscorePage class, handles showing the highscores.

        Args:
            root: 
                Base for tkinter, initializes the app view.
            handle_user_page: 
                Called variable to move to the user page.
        """

        self._root = root
        self._handle_user_page = handle_user_page
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

    def _initialize_info(self):
        info_text = "Below you can see highscores of the users in this computer."

        quiz_info = ttk.Label(
            master=self._frame,
            text=info_text
        )
        quiz_info.grid(row=0, column=0, padx=5, pady=10, sticky=constants.W)

    def _initialize_highscore(self):
        highscores = question_service.get_top_highscores()

        starting_row = 2

        if not highscores:
            highscore_label = ttk.Label(
                master=self._frame,
                text="No highscores available"
            )
            highscore_label.grid(row=starting_row, column=0, padx=5,
                                 pady=10, sticky=constants.W)

        else:
            ttk.Label(
                master=self._frame,
                text=f"Top 3 highscores out of total {len(self._questions)} points:"
            ).grid(row=starting_row, column=0, padx=5,
                   pady=10, sticky=constants.W)

            for idx, (username, points) in enumerate(highscores, start=1):
                ttk.Label(
                    master=self._frame,
                    text=f'{idx}. {username}: {points} points'
                ).grid(row=starting_row + idx, column=0, padx=5, pady=10, sticky=constants.W)

    def _initialize_user_page(self):
        style = ttk.Style(self._frame)
        style.configure('userpage.TButton',
                        foreground='white', background='grey')

        user_page_button = ttk.Button(
            master=self._frame,
            text="Return to user page",
            style='userpage.TButton',
            command=self._handle_user_page,

        )
        user_page_button.grid(row=0, column=1, padx=5,
                              pady=10, sticky=constants.NE)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_info()
        self._initialize_highscore()
        self._initialize_user_page()
        self._frame.grid_columnconfigure(0, weight=1)
