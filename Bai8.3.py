from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350*200')

lb1 = Label(window, text="Hello")

lb1.grid(column=0, row=0)

def clicked():
    lb1.configue(text="Button was clicked !!")

    btn = Button(window, text="Click Me", command=clicked)

    btn.grid(column=1, row=0)

    window.mainloop()
