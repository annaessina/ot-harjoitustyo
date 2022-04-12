import tkinter as tk

def add():

    number1 = entry1.get()
    number2 = entry2.get()

    sum = float(number1) + float(number2)
    lbl_result_add["text"] = f"{sum}"

def dist():

    number1 = entry1.get()
    number2 = entry2.get()

    distr = float(number1) - float(number2)
    lbl_result_dist["text"] = f"{distr}"

def mult():

    number1 = entry1.get()
    number2 = entry2.get()

    multi = float(number1) * float(number2)
    lbl_result_mult["text"] = f"{multi}"

def div():

    number1 = entry1.get()
    number2 = entry2.get()

    divis = float(number1) / float(number2)
    lbl_result_div["text"] = f"{divis}"


window = tk.Tk()
window.title("Calculator")

label1 = tk.Label(text="Enter number a:")
entry1 = tk.Entry()


label2 = tk.Label(text="Enter number b:")
entry2 = tk.Entry()


button_add = tk.Button(master=window, text="Calculate a + b", command=add)
lbl_result_add = tk.Label(master=window, text=" ")

button_dist = tk.Button(master=window, text="Calculate a - b", command=dist)
lbl_result_dist = tk.Label(master=window, text=" ")

button_mult = tk.Button(master=window, text="Calculate a * b", command=mult)
lbl_result_mult = tk.Label(master=window, text=" ")

button_div = tk.Button(master=window, text="Calculate a / b", command=div)
lbl_result_div = tk.Label(master=window, text=" ")


label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button_add.pack()
lbl_result_add.pack()
button_dist.pack()
lbl_result_dist.pack()
button_mult.pack()
lbl_result_mult.pack()
button_div.pack()
lbl_result_div.pack()

window.mainloop()