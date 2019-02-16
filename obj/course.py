class Course:

    grade = 0

    dist = [90, 80, 70, 60, 50]

    def __init__(self, name, assessments, credits):
        self.name = name
        self.assessments = assessments
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
            if self.assessments[k].completed:
                percentComplete += self.assessments[k].percentage
                grade += (sum(self.assessments[k].grades) / self.assessments[k].completed) * (
                    self.assessments[k].percentage)
        self.grade = grade / percentComplete
        print("current grade" + str(self.grade) + "\n")

    #next highest grade line
    def findTarget(self):
        for d in range(0, len(self.dist) - 2):
            if (self.grade > self.dist[d]) & (self.grade < self.dist[d+1]):
                return self.dist[d]

        return 100



    def minForNextGradeLine(self):
        target = self.findTarget()
        uncomplete = []
        uncompletedWeight = 0
        complete = []
        toSub = 0

        for a in self.assessments:
            if self.assessments[a].completed != self.assessments[a].total:
                uncomplete.append(a)
                uncompletedWeight += self.assessments[a].percentage
            else:
                complete.append(a)
                toSub = toSub + (self.assessments[a].percentage * sum(self.assessments[a].grades) / self.assessments[a].completed)

        target = (target*(1-uncompletedWeight)-toSub) / uncompletedWeight

        #return array of included assessments, avg score needed on future to move to next line, diff between this and avg
        return [uncomplete, target, target - self.grade]

        #do algebra








    def get_name(self):
        return self.name

    def add_asst(self, asst):
        self.assessments[asst.name] = asst

        self.calculateGrade()
