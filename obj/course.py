import os
from .Assessment import Assessment

class Course:

    grade = 0

    def __init__(self, name, credits):
        self.name = name
        self.assessments = {}
        self.credits = credits
        if len(self.assessments.keys()) > 0:
            self.grade = self.currentGrade()
        else:
            self.grade = None
        self.grade_dist = self.get_grade_dist()
        self.dist = self.grade_dist.keys()

    def add_asst(self, asst):
        if asst[0] in self.assessments:
            self.assessments[asst[0]].add_grade(float(asst[-1]))
        else:
            self.assessments[asst[0]] = Assessment(asst[0], asst[1], asst[2], asst[3])
            self.assessments[asst[0]].add_grade(float(asst[-1]))
        #self.calculateGrade()

    def print(self):
        print("------- {0} ------({1})".format(self.name, self.credits))
        print("--- Course Data ---")
        print("CURRENT GRADE %.2f" % self.currentGrade())
        for asst in self.assessments.keys():
            print("---AVG %s: - %.2f" % (self.assessments[asst].get_name(), self.assessments[asst].get_average()))

        print()
        for asst in self.assessments.keys():
            self.assessments[asst].print()

    def getGradeLetter(self):
        grades = self.grade_dist.keys()


    def get_grade_dist(self):
        dist = {}
        file = open("value-to-grade.txt", "r")
        for line in file.readlines():
            temp = line.split(',')
            dist[int(temp[1])] = temp[0]
        return dist

        # if len(self.assessments) != 0:
        #     self.calculateGrade()
        # else:
        #     self.grade = 0


    def currentGrade(self):
        grade = 0
        percentSum = 0
        for asst in self.assessments.keys():
            grade += self.assessments[asst].get_percentage() * self.assessments[asst].get_average()
            percentSum += self.assessments[asst].get_percentage()
        return grade / float(percentSum)



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

    def test_average(self):
        avg = 0
        for asst in self.assessments:
            avg += asst.get_percentage() / float(100) * asst.get_average()
        return avg
        self.assessments[asst.name] = asst

        self.calculateGrade()
