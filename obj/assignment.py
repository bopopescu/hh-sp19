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
