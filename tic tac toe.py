from tkinter import *

# Initialize the main window
window = Tk()
window.geometry("600x500+100+75")
window.title("Tic Tac Toe")

# Initialize variables
one = StringVar()
two = StringVar()
three = StringVar()
four = StringVar()
five = StringVar()
six = StringVar()
seven = StringVar()
eight = StringVar()
nine = StringVar()

lst = [""] * 9
user = "X"

# Function to switch users
def change_user():
    global user
    user = "O" if user == "X" else "X"

# Function to check for a winner
def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combo in winning_combinations:
        if lst[combo[0]] == lst[combo[1]] == lst[combo[2]] and lst[combo[0]] != "":
            result_label.config(text=f"Player {lst[combo[0]]} wins!")
            disable_buttons()
            return

    if all(lst):
        result_label.config(text="It's a tie!")
        disable_buttons()

# Function to handle button clicks
def play(n, var):
    if lst[n] == "":
        lst[n] = user
        var.set(user)
        check_winner()
        change_user()
    print(lst)

# Function to disable all buttons after game ends
def disable_buttons():
    for button in buttons:
        button.config(state=DISABLED)

# Function to reset the game
def reset_game():
    global lst, user
    lst = [""] * 9
    user = "X"
    one.set("")
    two.set("")
    three.set("")
    four.set("")
    five.set("")
    six.set("")
    seven.set("")
    eight.set("")
    nine.set("")
    result_label.config(text="")
    for button in buttons:
        button.config(state=NORMAL)

# Create buttons for the game board
buttons = [
    Button(window, textvariable=one, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(0, one)),
    Button(window, textvariable=two, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(1, two)),
    Button(window, textvariable=three, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(2, three)),
    Button(window, textvariable=four, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(3, four)),
    Button(window, textvariable=five, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(4, five)),
    Button(window, textvariable=six, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(5, six)),
    Button(window, textvariable=seven, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(6, seven)),
    Button(window, textvariable=eight, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(7, eight)),
    Button(window, textvariable=nine, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(8, nine))
]

# Place buttons on the window
buttons[0].place(x=0, y=0)
buttons[1].place(x=200, y=0)
buttons[2].place(x=400, y=0)
buttons[3].place(x=0, y=140)
buttons[4].place(x=200, y=140)
buttons[5].place(x=400, y=140)
buttons[6].place(x=0, y=280)
buttons[7].place(x=200, y=280)
buttons[8].place(x=400, y=280)

# Create a label to display the result
result_label = Label(window, text="", font=("arial", 20, "bold"))
result_label.place(x=0, y=420, width=600, height=50)

# Create a reset button
reset_button = Button(window, text="Reset Game", bg="#303F9F", fg="#FFFFFF", font=("arial", 20, "bold"), command=reset_game)
reset_button.place(x=200, y=470, width=200, height=50)

# Start the Tkinter event loop
window.mainloop()
