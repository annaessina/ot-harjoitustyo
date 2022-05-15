from ui.login import LogIn
from ui.create_new_user import CreateNew
from ui.calculator_window import CalculatorView


class Ui:
    """Class which is responsible for user interface """

    def __init__(self, root):
        """Constructor creates an entity of class to handle all ui functionality
        Args:
            root: Tkinter instance where user interface is initiated """
        self._root = root
        self._current_view = None

    def start(self):
        """Starts user interface"""
        self._login_window()

    def _login_window(self):
        """Shows main Log in window """
        self._hide_current_view()

        self._current_view = LogIn(
            self._root, self._calculator_window, self._create_window)
        self._current_view.pack()

    def _hide_current_view(self):
        """Hides current window"""
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _create_window(self):
        """Shows a window to create new user"""        

        self._hide_current_view()
        self._current_view = CreateNew(self._root, self._login_window)
        self._current_view.pack()

    def _calculator_window(self):
        """Shows a window with math functions to perfom"""
        self._hide_current_view()

        self._current_view = CalculatorView(self._root, self._login_window)
        self._current_view.pack()
    
