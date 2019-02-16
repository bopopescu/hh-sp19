class Course:

    grade = 0

    dist = [90, 80, 70, 60, 50]

    def __init__(self, name, credits):
        self.name = name
        self.assessments = {}
        self.credits = credits

    #next highest grade line
    def findTarget(self):
        for d in len(self.dist) - 2:
            if self.grade > self.dist(d) && self.grade < self.dist(d+1):
                return self.dist(d)

        return 100



    def minForNextGradeLine(self):
        target = self.findTarget()
        uncomplete = []
        complete = []
        for a in self.assessments:
            if (a.completed != a.total):
                uncomplete.append(a)
            else:
                complete.append(a)
                target = target  - (a.weight * a.grade.sum())

        #do algebra







    def get_name(self):
        return self.name

    def add_asst(self, asst):
        if asst[0] in self.assessments:
            self.assessments[asst[0]].add_grades(asst[-1])
        else :
            self.assessments[asst[0]] = Assessment(asst[0], asst[1],
            )
        self.assessments.append(asst)

    def test_average(self):
        avg = 0
        for asst in self.assessments:
            avg += asst.get_percentage() / float(100) * asst.get_average()
        return avg
