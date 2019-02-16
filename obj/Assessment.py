class Assessment:
    def __init__(self, name, percentage, grades, total, completed, isMidterm):
        self.name = name
        self.percentage = percentage
        self.grades = grades
        self.total = total
        self.completed = completed
        self.isMidterm = isMidterm

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_name(self):
        return self.name
