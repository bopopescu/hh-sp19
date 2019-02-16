class Semester():
    def __init__(self, name, percentage, isCompleted):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def get_name(self):
        return self.name
