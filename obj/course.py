class Course:
    def __init__(self, name, credits):
        self.name = name
        self.assessments = {}
        self.credits = credits

    def get_name(self):
        return self.name

    def add_asst(self, asst):
        if asst[0] in self.assessments:
            self.assessments[asst[0]].add_grades(asst[-1])
        else :
            self.assessments[asst[0]] = Assessment(asst[0], asst[1],
            )
        self.assessments.append(asst)
