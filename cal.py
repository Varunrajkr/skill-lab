from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry("400x500")

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal_press():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = StringVar()
entry_box = Entry(window, textvariable=equation, font=('arial', 20, 'bold'), bd=10, insertwidth=4, width=14, borderwidth=4, justify=RIGHT)
entry_box.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]
for (text, row, col) in buttons:
    Button(window, text=text, padx=20, pady=20, font=('arial', 20, 'bold'), command=lambda t=text: press(t) if t != '=' else equal_press()).grid(row=row, column=col)

Button(window, text='Clear', padx=20, pady=20, font=('arial', 20, 'bold'), command=clear).grid(row=5, column=0, columnspan=4, sticky="nsew")

for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

window.mainloop()
