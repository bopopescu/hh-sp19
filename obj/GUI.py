from tkinter import *
import sqlite3 as sq

class GUI:
    top = Tk()
    # BEGIN GUI BOX.
    top.title("Study Helper")
    label = Label(top, text="by Spencer, Kaushik, and Stephanie").pack()

    #text = Text(top)
    #text.insert(INSERT, "by Spencer, Kaushik, and Stephanie")
    #text.pack()

    # END GUI BOX
    top.mainloop()