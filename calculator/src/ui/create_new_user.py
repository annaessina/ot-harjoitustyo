from tkinter import ttk, constants, StringVar
from services.calculator_services import calculator_services, UsernameError


class CreateNew():
    """Class which is responsible for functionality to create new user"""

    def __init__(self, root, login):
        """Constructor creates an entity of class to handle functionality
        for new user account creation
        Args:
            root: Tkinter instance where user interface is initiated,
            login: takes care of return to main log in window """
        self._root = root
        self._frame = None
        self._login = login
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._create()

    def pack(self):
        """Call for Pack Layout Manager """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Call to destroy window"""
        self._frame.destroy()

    def _create(self):
        """Creates window to enter new username and password """
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(master=self._frame)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_variable)
        self._error_label.grid(padx=5, pady=5)

        back = ttk.Button(master=self._frame, text="Back", command=self._login)
        back.grid(row=0, columnspan=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        create_label = ttk.Label(master=self._frame, text="Create new user")
        create_label.grid(row=1, columnspan=2,
                          sticky=constants.W, padx=5, pady=5)

        username_label = ttk.Label(
            master=self._frame, text="Enter new username: ")
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(row=2, column=0, padx=5, pady=5)
        self._username_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password_label = ttk.Label(master=self._frame, text="Enter password: ")
        self._password_entry = ttk.Entry(master=self._frame)
        password_label.grid(row=3, column=0, padx=5, pady=5)
        self._password_entry.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        create = ttk.Button(master=self._frame,
                            text="Create user", command=self._create_process)
        create.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

        self._hide_error()

    def _create_process(self):
        """Takes care of functionality to create new user """
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0:
            self._show_error("Enter your username")
            return
        if len(password) == 0:
            self._show_error("Enter your password")
            return

        try:
            calculator_services.create_user(username, password)
            self._login()
        except UsernameError:
            self._show_error("Incorrect username or password")

    def _show_error(self, message):
        """Shows error message
        Args:
            message: error message"""
        self._error_variable.set(message)
        self._error_label.grid(row=5, column=0, padx=5, pady=5)

    def _hide_error(self):
        """Hides error message"""
        self._error_label.grid_remove()
