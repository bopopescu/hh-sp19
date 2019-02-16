from tkinter import *
from obj import assignment
from obj import Course


def main():
    assignment(50)
    top = Tk()
    text = Text(top)
    text.insert(INSERT, "by Spencer, Kaushik, and Stephanie")
    text.pack()
    top.mainloop()


if __name__ == "__main__":
    main()

