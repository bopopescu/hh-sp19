from tkinter import *

import sqlite3 as sq
class GUI(Frame):
        top = Tk()
        # BEGIN GUI BOX.

        text = Text(top)
        text.pack()

        top.title("Study Helper")
        label = Label(top, text="by Spencer, Kaushik, and Stephanie").pack()

        # END GUI BOX
        top.mainloop()


