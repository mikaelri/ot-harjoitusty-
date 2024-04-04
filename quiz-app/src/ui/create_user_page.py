from tkinter import ttk, StringVar, constants
from services.user_service import user_service, UsernameExistsError

class CreateUserPage:
    """Class handling the create a new user page."""

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
        self._username_add = None
        self._password_add = None
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

        if len(username) == 0 or len(password) == 0:
            self._show_error("Please add username and password")
            return
        
        try:
            user_service.create_user(username, password)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error(f'Username {username} exists, choose a new one')
    
    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")

        self._add_user = ttk.Entry(master=self._frame)
        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._add_user.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")

        self._add_password = ttk.Entry(master=self._frame)
        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._add_password.grid(padx=5, pady=5, sticky=constants.EW)
    
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
            text="Login page",
            command=self._handle_show_login_page
        )

        create_user_button = ttk.Button(
            master=self._frame,
            text="Create",
            command=self._handle_create_user
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()
