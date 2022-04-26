from ui.login import LogIn
from ui.create_new_user import CreateNew
from ui.calculator_window import CalculatorView


class Ui:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._login_window()

    def _login_window(self):
        self._hide_current_view()

        self._current_view = LogIn(self._root, self._calculator_window, self._create_window)
        self._current_view.pack()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _create_window(self):
        self._hide_current_view()

        self._current_view = CreateNew(self._root, self._login_window)
        self._current_view.pack()

    def _calculator_window(self):
        self._hide_current_view()

        self._current_view = CalculatorView(self._root, self._login_window)
        self._current_view.pack()