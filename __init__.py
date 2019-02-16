from tkinter import *


def main():
    top = Tk()
    text = Text(top)
    text.insert(INSERT, "by Spencer, Kaushik, and Stephanie")
    text.pack()
    top.mainloop()


if __name__ == "__main__":
    main()

