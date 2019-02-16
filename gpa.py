
class Course:
    def __init__(self, name):
        self.name = name
        self.assessments = []

    def get_name(self):
        return self.name

    def add_asst(self, asst):
        self.assessments.append(asst)

class Assessment():
    def __init__(self, name, percentage):
        self.name = name
        self.percentage = percentage
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def set_grades(self, grades):
        self.grades = grades

    def get_name(self):
        return self.name


if __name__ == '__main__':
    num = int(input("Input Number of Subjects: "))
    subs = []
    for i in range(num):
        course_name = input("Name of Course #{}: ".format(i + 1))
        course = Course(course_name)
        asst_len = int(input("Input number of assessments for {}: ".format(course_name)))
        for j in range(asst_len):
            asst_name = input("Input name of asst #{} for {}: ".format(j, course_name)))
            asst_perc = int(input("Input percentage of {}".format(asst_name)))
            asst = Assessment(asst_name, asst_perc)



    for i in range(len(subs)):
        print(subs[i].get_name())
