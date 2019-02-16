class Course:
    def __init__(self, name, credits):
        self.name = name
        self.assessments = []
        self.credits = credits

    def get_name(self):
        return self.name

    def add_asst(self, asst):
        self.assessments.append(asst)

    def test_average(self):
        avg = 0
        for asst in self.assessments:
            avg += asst.get_percentage() / float(100) * asst.get_average()
        return avg
