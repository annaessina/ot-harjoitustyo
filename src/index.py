from tkinter import Tk
from ui.calculator_window import CalculatorView
from ui.login import LogIn
from ui.create_new_user import CreateNew
from ui.ui import Ui


def main():
    window = Tk()
    window.title("Calculator")

    ui_view = Ui(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
