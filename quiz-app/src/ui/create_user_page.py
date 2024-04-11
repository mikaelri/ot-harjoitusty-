from tkinter import ttk, StringVar, constants
from services.user_service import user_service
from services.user_service import (
    UsernameExistsError,
    InvalidCredentialsError,
    PasswordError,
    PasswordTooShortError
)


class CreateUserPage:
    """Class handling the create a new user page.

    Attributes:
        root: 
            base for Tkinter.
        handle_create_user: 
            called variable to move to create a new user page.
        handle_show_login_page:
            called variable to move to login page.  
    """

    def __init__(self, root, handle_create_user, handle_show_login_page):
        """ Contructor, creating a create a new user view.

        Args:
            root: 
                base for Tkinter.
            handle_create_user: 
                called variable to move to create a new user page.
            handle_show_login_page:
                called variable to move to login page.   
        """
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login_page = handle_show_login_page
        self._frame = None
        self._add_user = None
        self._add_password = None
        self._add_password2 = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Showing the view with Tkinter pack-method."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Deletes the current view."""
        self._frame.destroy()

    def _create_user_handler(self):
        username = self._add_user.get()
        password = self._add_password.get()
        password2 = self._add_password2.get()

        try:
            user_service.create_user(username, password, password2)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error("Username {username} exists, choose a new one")
        except InvalidCredentialsError:
            self._show_error("Username must be at least 3 characters")
        except PasswordError:
            self._show_error("Passwords must be the same")
        except PasswordTooShortError:
            self._show_error("Password must be at least 6 characters")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_add_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Add username")

        self._add_user = ttk.Entry(master=self._frame)
        username_label.grid(padx=5, pady=5, sticky=constants.N)
        self._add_user.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_add_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Add password")

        self._add_password = ttk.Entry(master=self._frame, show="*")
        password_label.grid(padx=5, pady=5, sticky=constants.N)
        self._add_password.grid(padx=5, pady=5, sticky=constants.EW)

        password2_label = ttk.Label(
            master=self._frame, text="Add password again")

        self._add_password2 = ttk.Entry(master=self._frame, show="*")
        password2_label.grid(padx=5, pady=5, sticky=constants.N)
        self._add_password2.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        self._initialize_add_username_field()
        self._initialize_add_password_field()

        create_user_button = ttk.Button(
            master=self._frame,
            text="Create a new user",
            command=self._create_user_handler
        )
        login_button = ttk.Button(
            master=self._frame,
            text="Go to Login page",
            command=self._handle_show_login_page
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        create_user_button.grid(padx=5, pady=10, sticky=constants.EW)
        login_button.grid(padx=5, pady=10, sticky=constants.EW)

        self._hide_error()
