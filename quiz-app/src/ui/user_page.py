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

    def _quiz_handler(self):
        pass
        # this will be function to start the quiz TBD

    def _logout_handler(self):
        user_service.logout()
        self._handle_logout()

    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame, text=f'Logged in as {self._user.username}')
        user_label.grid(row=0, column=0, padx=5, pady=10, sticky=constants.N)

    def _initialize_new_quiz(self):
        start_quiz_button = ttk.Button(
            master=self._frame,
            text="Start a new quiz",
            command=self._handle_start_quiz
        )
        start_quiz_button.grid(row=1, padx=5, pady=10, sticky=constants.EW)

    def _initialize_logout(self):
        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._logout_handler)
        logout_button.grid(padx=5, pady=10, sticky=constants.EW)

    def _initialize_footer(self):
        pass

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_new_quiz()
        self._initialize_header()
        self._initialize_logout()
        self._frame.grid_columnconfigure(0, weight=1)
