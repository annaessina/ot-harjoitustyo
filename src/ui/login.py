from tkinter import ttk, constants, StringVar
from services.calculator_services import calculator_services, InvalidUsernameOrPasswordError

class LogIn():
    """Class which is responsible for authentification of users"""
    def __init__(self, root, handle_login, create_user):
        """Constructor creates an entity of class to handle functionality
        for user authentification
        Args:
            root: Tkinter instance where user interface is initiated,
            handle_login: takes care of log in functionality,
            create_user: create new user account window """
        self._root = root
        self._handle_create_user = create_user
        self._handle_login = handle_login
        self._frame = None
        self._username_entry = None
        self._error_variable = None
        self._error_label = None

        self._login()

    def pack(self):
        """Call for Pack Layout Manager """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Call to destroy window"""
        self._frame.destroy()

    def _login(self):
        """Main window to start log in process is created """
        self._frame = ttk.Frame(master= self._root)

        self._error_variable = StringVar(master= self._frame)
        self._error_label = ttk.Label(master= self._frame, textvariable= self._error_variable)
        self._error_label.grid(padx= 5, pady= 5)

        login_label = ttk.Label(master=self._frame, text= "If you are already registered, type in your name and password")
        login_label.grid(row= 0, column= 0, sticky=constants.W, padx=5, pady=5)

        username_label = ttk.Label(master=self._frame, text= "Name:")
        username_label.grid(row= 1, column= 0, padx=5, pady=5)
        self._username_entry = ttk.Entry(master=self._frame)
        self._username_entry.grid(row= 2, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label = ttk.Label(master=self._frame, text= "Password:")
        password_label.grid(row= 3, column= 0, padx=5, pady=5)
        self._password_entry = ttk.Entry(master=self._frame)
        self._password_entry.grid(row=4, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)

        enter = ttk.Button(master=self._frame, text= "Log in", command= self._login_process)
        enter.grid(row= 5, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        create_label = ttk.Label(master=self._frame, text= "If this is your first visit, you need to create an account")
        create_label.grid(row= 7, column= 0, sticky=constants.W, padx=5, pady=5)


        self._frame.grid_columnconfigure(0, weight=1, minsize=300)

        create_user_button = ttk.Button(master=self._frame, text= "Proceed to create new account", command= self._handle_create_user)
        create_user_button.grid(row= 8, columnspan= 2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._hide_error()

    def _login_process(self):
        """Checks whether name and password are entered and proceeds for authentification"""
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0:
            self._show_error("Name is missing. Enter it again.")
            return

        if len(password) == 0:
            self._show_error("Password is mising. Enter it again.")
            return

        try:
            calculator_services.login(username, password)
            self._handle_login()

        except InvalidUsernameOrPasswordError:
            self._show_error("Incorrect name or password")

    def _show_error(self, message):
        """Shows error message
        Args:
            message: error message"""
        self._error_variable.set(message)
        self._error_label.grid(row= 0, column= 1, padx= 5, pady= 5)

    def _hide_error(self):
        """Hides error message"""
        self._error_label.grid_remove()