from obj import *
import os


def print_all(couses):
    for key in courses.keys():
        courses[key].print()
        print()


if __name__ == '__main__':
    #opens gpa_data.txt file and checks if it is empty
    gpa_data = open("gpa_data.txt", "r+")
    isEmpty = False
    if (os.stat("gpa_data.txt").st_size == 0):
        isEmpty = True

    #course, credits, assignment, weight, grade
    courses = {}

    if (not isEmpty):
        lines = gpa_data.readlines()
        for line in lines:
            description = line.split(",")
            if description[0] in courses:
                courses[description[0]].add_asst(description[2:])
            else:
                temp = Course(description[0], int(description[1]))
                courses[description[0]] = temp
                courses[description[0]].add_asst(description[2:])

    print("What would you like to do?")
    print("1) Add a grade.")
    print("2) Look at grades.\n")

    input = int(input("Please select 1 or 2 to continue: "))

    if (input == 1):
        print("Which class would you like to add a grade to?")

    elif (input == 2):
        print_all(courses)
