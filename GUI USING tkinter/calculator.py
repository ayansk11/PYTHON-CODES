#   
#   @author [Ayan Shaikh]
#   @email [ayaansk152@gmail.com]
#   @create date 2023-07-17 11:13:18
#   @modify date 2023-07-17 11:15:00
#   @desc [Basic Calulator using Tkinter]
#   

import tkinter as tk

window = tk.Tk()
window.title = "CALCULATOR"

window.geometry("400x180")                           # Setting the size of the Tkinter window 
window.eval('tk::PlaceWindow . center')              # Placing the Tkinter window at center of the screen

result_entry = tk.Entry(window, width=30)
result_entry.grid(row=0, column=0, columnspan=4)

operation = {
    "current": "",
    "value": 0
}

def add():

    num1 = float(result_entry.get())
    result_entry.delete(0, tk.END)
    operation["current"] = "add"
    operation["value"] = num1

def sub():

    num1 = float(result_entry.get())
    result_entry.delete(0, tk.END)
    operation["current"] = "sub"
    operation["value"] = num1

def multiply():

    num1 = float(result_entry.get())
    result_entry.delete(0, tk.END)
    operation["current"] = "multiply"
    operation["value"] = num1

def divide():

    num1 = float(result_entry.get())
    result_entry.delete(0, tk.END)
    operation["current"] = "divide"
    operation["value"] = num1

def calculate():

    num2 = float(result_entry.get())
    result_entry.delete(0, tk.END)

    if operation["current"] == "add":
        result = operation["value"] + num2

    elif operation["current"] == "sub":
        result = operation["value"] - num2

    elif operation["current"] == "multiply":
        result = operation["value"] * num2      

    elif operation["current"] == "divide":

        if num2 != 0:
            result = operation["value"] / num2 

        else: 
            result = "Error: Division by zero"

    else:
        result = num2
    
    result_entry.insert(tk.END, result)

digits = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0"]

row_index = 1
col_index = 0

for digit in digits:

    button = tk.Button(window, text=digit, width=7, command=lambda digit=digit: result_entry.insert(tk.END, digit))
    button.grid(row=row_index, column=col_index)
    col_index += 1

    if col_index > 2:

        col_index = 0
        row_index += 1

button_add = tk.Button(window, text="+", width=7, command=add)
button_add.grid(row=1, column=3)

button_sub = tk.Button(window, text="-", width=7, command=sub)
button_sub.grid(row=2, column=3)

button_multiply = tk.Button(window, text="*", width=7, command=multiply)
button_multiply.grid(row=3, column=3)

button_divide = tk.Button(window, text="/", width=7, command=divide)
button_divide.grid(row=4, column=3)

button_equal = tk.Button(window, text="=", width=7, command=calculate)
button_equal.grid(row=4, column=2)

window.mainloop()