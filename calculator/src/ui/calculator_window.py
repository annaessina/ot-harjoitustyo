from tkinter import ttk, constants, StringVar, Listbox, Scrollbar
from services.calculator_services import calculator_services
from repositories.record_repository import record_repository


class CalculatorView():
    """Class which is responsible for functionality of math operations"""

    def __init__(self, root, handle_logout): #, purchases_view):
        """Constructor creates an entity of class to handle functionality
        of math operations
        Args:
            root: Tkinter instance where user interface is initiated,
            handle_logout: takes care of log out functionality """
        self._root = root
        self._frame = None
        self._handle_logout = handle_logout
        self._user = calculator_services.get_current_user()
        self._username = calculator_services.get_current_user().username

        self.calculator_view()

    def pack(self):
        """Call for Pack Layout Manager """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Call to destroy window"""
        self._frame.destroy()

    def calculator_view(self):
        """Window is created to perform math operations"""
        self._frame = ttk.Frame(master=self._root)

        self._window_label = ttk.Label(
            master=self._frame, text="Calculate four basic operations in math: Addition, Subtraction, Multiplication and Division")
        self._window_label.grid(row=0, column=0, padx=5, pady=5)

        logout_button = ttk.Button(
            master=self._frame, text="Log out", command=self._handle_logout)
        logout_button.grid(row=0, column=5, padx=5,
                           pady=5, sticky=constants.EW)

        delete_user_button = ttk.Button(
            master=self._frame, text="Delete user", command=self.delete_process)
        delete_user_button.grid(row=1, column=5, padx=5,
                                pady=5, sticky=constants.EW)

        

        number1_label = ttk.Label(master=self._frame, text= "Enter number a:")
        number1_label.grid(row=3, column= 0, padx=5, pady=5)
        self._number1_entry = ttk.Entry(master=self._frame)
        self._number1_entry.grid(row=4, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)

        number2_label = ttk.Label(master=self._frame, text= "Enter number b:")
        number2_label.grid(row=5, column= 0, padx=5, pady=5)
        self._number2_entry = ttk.Entry(master=self._frame)
        self._number2_entry.grid(row=6, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)



        btn_add = ttk.Button(master=self._frame, text="Calculate  a + b =", command= self._add_process)
        btn_add.grid(row=7, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._lbl_result_add = ttk.Label(master=self._frame, text=" ")
        self._lbl_result_add.grid(row=7, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        btn_dist = ttk.Button(master=self._frame, text="Calculate  a - b =", command= self._dist_process)
        btn_dist.grid(row=8, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._lbl_result_dist = ttk.Label(master=self._frame, text=" ")
        self._lbl_result_dist.grid(row=8, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        btn_mult = ttk.Button(master=self._frame, text="Calculate  a * b =", command= self._mult_process)
        btn_mult.grid(row=9, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._lbl_result_mult = ttk.Label(master=self._frame, text=" ")
        self._lbl_result_mult.grid(row=9, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        btn_div = ttk.Button(master=self._frame, text="Calculate  a / b =", command= self._div_process)
        btn_div.grid(row=10, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._lbl_result_div = ttk.Label(master=self._frame, text=" ")
        self._lbl_result_div.grid(row=10, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)


        self._editview_label = ttk.Label(
            master=self._frame, text="Save data to database: ")
        self._editview_label.grid(
            row=12, column=0, padx=5, pady=5, sticky=constants.EW)

        editview_button = ttk.Button(
            master=self._frame, text="Save data", command=self.add_record_to_database_process)  
        editview_button.grid(row=12, column=1, padx=5,
                             pady=5, sticky=constants.EW)




    def add_record_to_database_process(self):
        """Adds new record to database"""
        
        if self.number1 == 0:
            self._show_error("Enter number1!")
            return
        if self.number2 == 0:
            self._show_error("Enter number2!")
            return

        calculator_services.add_record(self.number1, self.number2, self.add2, self.dist, self.mult, self.div, self._username)
        

    
    def _add_process(self):
        """Performs addtion"""
        self.number1 = self._number1_entry.get()
        self.number2 = self._number2_entry.get()

        self.add2 = float(self.number1) + float(self.number2)
        self._lbl_result_add["text"] = f"{self.add2}"
        

    def _dist_process(self):
        """Performs distraction"""
        self.number1 = self._number1_entry.get()
        self.number2 = self._number2_entry.get()

        self.dist = float(self.number1) - float(self.number2)
        self._lbl_result_dist["text"] = f"{self.dist}"

    def _mult_process(self):
        """Performs multiplication"""
        self.number1 = self._number1_entry.get()
        self.number2 = self._number2_entry.get()

        self.mult = float(self.number1) * float(self.number2)
        self._lbl_result_mult["text"] = f"{self.mult}"

    def _div_process(self):
        """Performs division"""
        self.number1 = self._number1_entry.get()
        self.number2 = self._number2_entry.get()

        self.div = float(self.number1) / float(self.number2)
        self._lbl_result_div["text"] = f"{self.div}"



    def delete_process(self):
        """Takes care of deletion of user data"""
        calculator_services.delete_user(self._user.username)

        self._handle_logout()
