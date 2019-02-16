class Assessment():
    def __init__(self, name, percentage, total, isMidterm):
        self.name = name
        self.percentage = percentage
        self.grades = []
        #self.total = total
        self.completed = 0
        self.isMidterm = isMidterm

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_name(self):
        return self.name
