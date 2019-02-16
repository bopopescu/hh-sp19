
from obj import assignment
from obj import GUI
import sqlite3 as sq
from obj import Course


def main():
    db = sq.connect('data/mydb')
    # ALL DATABASE CONNECTIONS BELOW HERE

    assignment(50)

    GUI()

    #ALL DATABASE CONNECTIONS ABOVE HERE
    db.close()


if __name__ == "__main__":
    main()

