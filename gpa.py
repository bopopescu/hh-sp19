import obj
import os

if __name__ == '__main__':
    #opens gpa_data.txt file and checks if it is empty
    gpa_data = open("gpa_data.txt", "r+")
    isEmpty = False
    if (os.stat("gpa_data.txt").st_size == 0):
        isEmpty = True

    #course, credits, assignment, weight, grade
    courses = {}

    if (not isEmpty):
        line = gpa_data.readline()

        while line:
            descriptions = line.split(",")

            if description[0] in courses:
                courses[description[0]].add_asst(description[2:])
            else:
                temp = Course(descriptions[0], descriptions[1])
                courses.append(temp)
                courses.[description[0]].add_asst(description[2:])

            line = gpa_data.readline()



    print("What would you like to do?")
    print("1) Add a grade.")
    print("2) Look at grades.\n")

    input = int(input("Please select 1 or 2 to continue: "))

    if (input == 1):
        print("Which class would you like to add a grade to?")


    # num = int(input("Input Number of Subjects: "))
    # subs = []
    # for i in range(num):
    #     course_name = input("Name of Course #{}: ".format(i + 1))
    #     course = Course(course_name)
    #     asst_len = int(input("Input number of assessments for {}: ".format(course_name)))
    #     for j in range(asst_len):
    #         asst_name = input("Input name of asst #{} for {}: ".format(j, course_name)))
    #         asst_perc = int(input("Input percentage of {}".format(asst_name)))
    #         asst = Assessment(asst_name, asst_perc)
    #
    #
    #
    # for i in range(len(subs)):
    #     print(subs[i].get_name())
    #
