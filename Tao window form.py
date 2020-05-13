from tkinter import *

def Newfile():
    printer("New File!")
def About():
    printer("This is a simple example of a menu")

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=Newfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmeny = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()
