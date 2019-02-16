
from obj import assignment
from obj import GUI
import sqlite3 as sq
from obj import Course


def main():
    db = sq.connect('data/mydb')
    # ALL DATABASE CONNECTIONS BELOW HERE

    #for testing
    A1 = assignment("midterm1", 20, 82, 1, 1, True)
    A2 = assignment("midterm2", 20, 86, 1, 1, True)
    A3 = assignment("midterm3", 20, 0, 1, 0, True)
    F = assignment("final", 30, 0, 1, 0, True)
    HW = assignment("homework", 10, 92, 10, 6, False)

    assignments = {
                      "midterm1": A1,
                      "midterm2": A2,
                      "midterm3": A3,
                      "final": F,
                      "homework": HW
    }

    testCourse = Course("biology", assignments, 3)

    print(testCourse.minForNextGradeLine())

    GUI()

    #ALL DATABASE CONNECTIONS ABOVE HERE
    db.close()


if __name__ == "__main__":
    main()

