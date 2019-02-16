class Course:
    def __init__(self, name, credits):
        self.name = name
        self.assessments = []
        self.credits = credits

    def get_name(self):
        return self.name

    def add_asst(self, asst):
        self.assessments.append(asst)
