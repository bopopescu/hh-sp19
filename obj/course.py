class Course:

    grade = 0

    dist = [90, 80, 70, 60, 50]

    def __init__(self, name, credits):
        self.name = name
        self.assessments = {}
        self.credits = credits

        if len(self.assessments) != 0:
            self.calculateGrade()
        else:
            self.grade = 0

    def calculateGrade(self):
        percentComplete = 0
        grade = 0
        # recalculate grade
        for k in self.assessments:
            percentComplete += self.assessments[k].percentage
            grade += (self.assessments[k].grades.sum() / self.assessments[k].completed) * (
                self.assessments[k].percentage)
        self.grade = grade / percentComplete

    #next highest grade line
    def findTarget(self):
        for d in len(self.dist) - 2:
            if self.grade > self.dist(d) & self.grade < self.dist(d+1):
                return self.dist(d)

        return 100



    def minForNextGradeLine(self):
        target = self.findTarget() * len(self.assessments)
        uncomplete = []
        uncompletedWeight = 0
        complete = []
        for a in self.assessments:
            if (a.completed != a.total):
                uncomplete.append(a)
                uncompletedWeight += a.weight
            else:
                complete.append(a)
                target = target  - (a.weight * a.grade.sum())

        target = target / uncompletedWeight

        #return array of included assessments, avg score needed on future to move to next line, diff between this and avg
        return [uncomplete, target, target - self.grade]

        #do algebra








    def get_name(self):
        return self.name

    def add_asst(self, asst):
        self.assessments[asst.name] = asst

        self.calculateGrade()