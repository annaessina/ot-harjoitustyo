import tkinter as tk

def add():

    number1 = entry1.get()
    number2 = entry2.get()

    sum = float(number1) + float(number2)
    lbl_result["text"] = f"{sum}"


window = tk.Tk()
window.title("Calculator")

label1 = tk.Label(text="Enter first number:")
entry1 = tk.Entry()


label2 = tk.Label(text="Enter second number:")
entry2 = tk.Entry()


button = tk.Button(master=window, text="Calculate sum", command=add)
lbl_result = tk.Label(master=window, text=" ")

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button.pack()
lbl_result.pack()

window.mainloop()