import os

class Course:

    grade = 0

    dist = [90, 80, 70, 60, 50]

    def __init__(self, name, assessments, credits):
        self.name = name
        self.assessments = assessments
        self.credits = credits
        self.grade_dist = get_grade_dist()
        self.dist = self.grade_dist.keys()

    def get_grade_dist(self):
        dist = {}
        file = open("value-to-gpa.txt", "r")
        for line in file.readlines():
            temp = line.split('')
            dist[int(temp[1])] = temp[0]
        return dist

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

    #next highest grade line
    def findTarget(self):
        for d in range(0, len(self.dist) - 2):
            if (self.grade > self.dist[d]) & (self.grade < self.dist[d+1]):
                return self.dist[d]

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
                target = target  - (sum(a.weight * a.grade))

        target = target / uncompletedWeight

        #return array of included assessments, avg score needed on future to move to next line, diff between this and avg
        return [uncomplete, target, target - self.grade]

        #do algebra








    def get_name(self):
        return self.name

    def add_asst(self, asst):
<<<<<<< HEAD
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
=======
        self.assessments[asst.name] = asst

        self.calculateGrade()
>>>>>>> 8eef5b735a8719693bb85157f059bc1f6b5ebf47
