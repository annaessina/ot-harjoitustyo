from tkinter import ttk, constants, StringVar, Listbox, Scrollbar
from services.calculator_services import calculator_services
from repositories.calculator_repository import calculator_repository


class CalculatorView():
    """Class which is responsible for functionality of math operations"""
    def __init__(self, root, handle_logout):
        """Constructor creates an entity of class to handle functionality
        of math operations
        Args:
            root: Tkinter instance where user interface is initiated,
            handle_logout: takes care of log out functionality """
        self._root = root
        self._frame = None
        self._handle_logout = handle_logout
        #self._handle_purchases_view = purchases_view
        self._user = calculator_services.get_current_user()

        self.calculator_view()

    def pack(self):
        """Call for Pack Layout Manager """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Call to destroy window"""
        self._frame.destroy()

    def calculator_view(self):
        """Windows is created to perform math operations"""
        self._frame = ttk.Frame(master=self._root)

        self._window_label = ttk.Label(
            master=self._frame, text="Calculate four basic operations in math: Addition, Subtraction, Multiplication and Division")
        self._window_label.grid(row=0, column=0, padx=5, pady=5)

        numberA_label = ttk.Label(master=self._frame, text= "Enter number a:")
        numberA_label.grid(row=1, column= 0, padx=5, pady=5)
        self._numberA_entry = ttk.Entry(master=self._frame)
        self._numberA_entry.grid(row=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)

        numberB_label = ttk.Label(master=self._frame, text= "Enter number b:")
        numberB_label.grid(row= 3, column= 0, padx=5, pady=5)
        self._numberB_entry = ttk.Entry(master=self._frame)
        self._numberB_entry.grid(row=4, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)



        button_add = ttk.Button(master=self._frame, text="Calculate  a + b ", command= self._add_process)
        button_add.grid(row= 5, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._lbl_result_add = ttk.Label(master=self._frame, text=" ")
        #self._lbl_result_add.grid(row= 5, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        button_dist = ttk.Button(master=self._frame, text="Calculate  a - b ", command= self._dist_process)
        button_dist.grid(row= 6, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._lbl_result_dist = ttk.Label(master=self._frame, text=" ")
        #self._lbl_result_dist.grid(row= 5, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        button_mult = ttk.Button(master=self._frame, text="Calculate  a * b ", command= self._mult_process)
        button_mult.grid(row= 7, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._lbl_result_mult = ttk.Label(master=self._frame, text=" ")
        #self._lbl_result_mult.grid(row= 5, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        button_div = ttk.Button(master=self._frame, text="Calculate  a / b ", command= self._div_process)
        button_div.grid(row= 8, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._lbl_result_div = ttk.Label(master=self._frame, text=" ")
        #self._lbl_result_div.grid(row= 5, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)


        logout_button = ttk.Button(
            master=self._frame, text="Log out", command=self._handle_logout)
        logout_button.grid(row=0, column=5, padx=5,
                           pady=5, sticky=constants.EW)

        delete_user_button = ttk.Button(master=self._frame, text="Delete user", command= self.delete_process)
        delete_user_button.grid(row=1, column=5, padx=5,
                                pady=5, sticky=constants.EW)


    def _add_process(self):
        """Performs addition"""
        numberA = self._numberA_entry.get()
        numberB = self._numberB_entry.get()

        sum = float(numberA) + float(numberB)
        lbl_result_add["text"] = f"{sum}"

    def _dist_process(self):
        """Performs distraction"""
        numberA = self._numberA_entry.get()
        numberB = self._numberB_entry.get()

        dist = float(numberA) - float(numberB)
        lbl_result_dist["text"] = f"{dist}"

    def _mult_process(self):
        """Performs multiplication"""
        numberA = self._numberA_entry.get()
        numberB = self._numberB_entry.get()

        mult = float(numberA) * float(numberB)
        lbl_result_mult["text"] = f"{mult}"

    def _div_process(self):
        """Performs division"""
        numberA = self._numberA_entry.get()
        numberB = self._numberB_entry.get()

        div = float(numberA) / float(numberB)
        lbl_result_div["text"] = f"{div}"



    def delete_process(self):
        """Takes care of deletion of user data"""
        calculator_services.delete_user(self._user.username)

        self._handle_logout()