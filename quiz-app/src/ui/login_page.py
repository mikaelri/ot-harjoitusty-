from tkinter import ttk, StringVar, constants
from services.user_service import user_service, InvalidCredentialsError


class LoginPage:
    """Class handling the user login page.
    Attributes:
        root: 
            base for Tkinter.
        handle_login: 
            called variable to move to login page.
        handle_create_user:
            called variable to move to create a new user page. 
    """

    def __init__(self, root, handle_login, handle_create_user_page):
        """ Contructor, creating a new login view.

        Args:
            root: 
                base for Tkinter.
            handle_login: 
                called variable to move to login page.
            handle_create_user:
                called variable to move to create a new user page.   
        """
        self._root = root
        self._handle_login = handle_login
        self._handle_create_user_page = handle_create_user_page
        self._frame = None
        self._add_user = None
        self._add_password = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Showing the view with Tkinter pack-method."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Deletes the current view."""
        self._frame.destroy()

    def _login_handler(self):
        username = self._add_user.get()
        password = self._add_password.get()

        try:
            user_service.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            self._show_error("Invalid credentials, try again")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        username_label.grid(row=2, padx=5, pady=5, sticky=constants.N)

        self._add_user = ttk.Entry(master=self._frame, width=50)
        self._add_user.grid(padx=5, pady=5)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")

        self._add_password = ttk.Entry(master=self._frame, show="*", width=50)
        password_label.grid(padx=5, pady=5, sticky=constants.N)
        self._add_password.grid(padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()

        login_button = ttk.Button(
            master=self._frame,
            width=50,
            text="Login",
            command=self._login_handler
        )

        create_user_button = ttk.Button(
            master=self._frame,
            width=50,
            text="Go to Create a new user page",
            command=self._handle_create_user_page
        )

        self._frame.grid_columnconfigure(0, weight=1)

        login_button.grid(padx=5, pady=10)
        create_user_button.grid(padx=5, pady=10)

        self._hide_error()
