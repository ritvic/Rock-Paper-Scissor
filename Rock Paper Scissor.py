# import required libraries
from tkinter import *
import random

#  Create an instance of tkinter frame
root = Tk()

# Set the geometry of the window
root.geometry("750x450")

# Fix the window size
root.resizable(0, 0)

# Set the title of the window
root.title("Rock Paper Scissors....")

# Default value for Computer
computer_options = {"0": "Rock", "1": "Paper", "2": "Scissor"}


# exit the window
def iexit():
    root.destroy()


# Disable all the Buttons after first Match
def button_disable():
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")


# Define function for Rock
def isrock():
    value = computer_options[str(random.randint(0, 2))]
    if value == "Rock":
        match_result = "Match Draw!"
    elif value == "Scissor":
        match_result = "Wohoo! You Won!"
    else:
        match_result = "Alas!! You Lose!"
    label.config(text=match_result)
    l1.config(text="Rock")
    l3.config(text=value)
    button_disable()


# Function for Paper
def ispaper():
    value = computer_options[str(random.randint(0, 2))]
    if value == "Paper":
        match_result = "Match Draw!"
    elif value == "Scissor":
        match_result = "Computer Win:("
    else:
        match_result = "Amazingg..You won!"
    label.config(text=match_result)
    l1.config(text="Paper")
    l3.config(text=value)
    button_disable()


# Function for Scissor
def isscissor():
    value = computer_options[str(random.randint(0, 2))]
    if value == "Rock":
        match_result = "You Lose...:("
    elif value == "Scissor":
        match_result = "Match Draw!"
    else:
        match_result = "You Won... :D"
    label.config(text=match_result)
    l1.config(text="Scissor")
    l3.config(text=value)
    button_disable()


# Reset the Game
def reset():
    b1.config(state="active")
    b2.config(state="active")
    b3.config(state="active")
    l1.config(text="Player")
    l3.config(text="Computer")
    label.config(text="")


# Create a LabelFrame
labelframe = LabelFrame(root, text="Rock Paper Scissor", font='Arial 20 bold', labelanchor="n", bd=10, bg="thistle2",
                        width=600, height=50, cursor="pirate")
labelframe.pack(expand=True, fill=BOTH)

# Label for Player
l1 = Label(labelframe, text="Player", font='Georgia 18 bold')
l1.place(relx=.18, rely=.1)

# Label for VS
l2 = Label(labelframe, text="VS", font='Georgia 18 bold', bg="thistle2")
l2.place(relx=.45, rely=.1)

# Label for Computer
l3 = Label(labelframe, text="Computer", font='Georgia 18 bold')
l3.place(relx=.65, rely=.1)

# Create a label to display the Conditions
label = Label(labelframe, text="", font=('Coveat', 25, 'bold'), bg="thistle2")
label.pack(pady=150)

# Create Button Set for Rock, Paper and Scissor
b1 = Button(labelframe, text="Rock", font=10, width=7, command=isrock)
b1.place(relx=.27, rely=.62)
b2 = Button(labelframe, text="Paper", font=10, width=7, command=ispaper)
b2.place(relx=.42, rely=.62)
b3 = Button(labelframe, text="Scissor", font=10, width=7, command=isscissor)
b3.place(relx=.57, rely=.62)

# Button to reset the Game
reset = Button(labelframe, text="Reset", bg="Red2", fg="white", width=7, font='10', command=reset)
reset.place(relx=.32, rely=.82)
Button(labelframe, text="Exit", bg="Red2", fg="white", width=7, font='10', command=iexit).place(relx=.52, rely=.82)
root.mainloop()
