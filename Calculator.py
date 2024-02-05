import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete("1.0", "end")
    text_result.insert("1.0", calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete("1.0", "end")
        text_result.insert("1.0", calculation)
    except:
        clear_field()
        text_result.insert("1.0", "Error")
        pass

def clear_field():
    global calculation
    calculation = ""
    text_result.delete("1.0", "end")


root = tk.Tk()

# Main window
root.geometry("300x275")

#Text result text
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))

#Text result grid. This allows the grid to span across all 5 columns.
text_result.grid(columnspan=5)

#Numbers
#1
button1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
button1.grid(row=2, column=1)
#2
button2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
button2.grid(row=2, column=2)
#3
button3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
button3.grid(row=2, column=3)
#4
button4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
button4.grid(row=3, column=1)
#5
button5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
button5.grid(row=3, column=2)
#6
button6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
button6.grid(row=3, column=3)
#7
button7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
button7.grid(row=4, column=1)
#8
button8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
button8.grid(row=4, column=2)
#9
button9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
button9.grid(row=4, column=3)
#0
button0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
button0.grid(row=5, column=2)

#Operators
#Plus
button_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
button_plus.grid(row=2, column=4)
#Minus
button_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
button_minus.grid(row=3, column=4)
#Multiply
button_multiply = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
button_multiply.grid(row=4, column=4)
#Divide
button_divide = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
button_divide.grid(row=5, column=4)

#Other buttons
#Open parenthesis
button_open_parenthesis = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
button_open_parenthesis.grid(row=5, column=1)
#Close parenthesis
button_close_parenthesis = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
button_close_parenthesis.grid(row=5, column=3)
#Equals
button_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14))
button_equals.grid(row=6, column=3, columnspan=2)
#Clear
button_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial", 14))
button_clear.grid(row=6, column=1, columnspan=2)



root.mainloop()
    