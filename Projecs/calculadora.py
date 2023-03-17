from tkinter import *

# Define the main window
root = Tk()
root.title("Calculator")

# Create the input field
input_field = Entry(root, width=35, borderwidth=5)
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define functions for calculator operations
def click(number):
    current = input_field.get()
    input_field.delete(0, END)
    input_field.insert(0, str(current) + str(number))

def clear_input_field():
    input_field.delete(0, END)

def addition():
    first_number = input_field.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = float(first_number)
    input_field.delete(0, END)

def subtraction():
    first_number = input_field.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(first_number)
    input_field.delete(0, END)

def multiplication():
    first_number = input_field.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first_number)
    input_field.delete(0, END)

def division():
    first_number = input_field.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(first_number)
    input_field.delete(0, END)

def equal():
    second_number = input_field.get()
    input_field.delete(0, END)
    if math_operation == "addition":
        input_field.insert(0, f_num + float(second_number))
    elif math_operation == "subtraction":
        input_field.insert(0, f_num - float(second_number))
    elif math_operation == "multiplication":
        input_field.insert(0, f_num * float(second_number))
    elif math_operation == "division":
        input_field.insert(0, f_num / float(second_number))

# Create the number buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: click(0))

# Add the number buttons to the GUI
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

# Create the operation buttons
button_add = Button(root, text="+", padx=39, pady=20, command=addition)
button_subtract = Button(root, text="-", padx=40, pady=20, command=subtraction)
button_multiply = Button(root, text="*", padx=41, pady=20, command=multiplication)
button_divide = Button(root, text="/", padx=41, pady=20, command=division)
button_equal = Button(root, text="=", padx=39, pady=52, command=equal)
button_clear = Button(root, text="Clear", padx=77, pady=20, command=clear_input_field)

# Add the operation buttons to the GUI
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=6, column=1)
button_equal.grid(row=5, column=2, rowspan=2)

# Run the program
root.mainloop()
