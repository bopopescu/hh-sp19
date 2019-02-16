class optimalChange:

    def __init__(self):
        self.Courses = []

    def addCourse(self, course):
        self.Courses.append(course)

    def getTestAvg(self, course):
        return course.getTestAvg()

    def getCourseAvg(self, course):
        return course.getAvg()

    def getGPA(self):
        count = 0
        for course in self.Courses:
            count += course.getAvg()
        return count / len(self.Courses)

    def find(self):
        best = []
        for course in self.Courses:
            arr = course.minForNextGradeLine()
            temp = arr[3]
            if temp < best[3]:
                best = [course, arr, temp]





    print("will give best thing to improve")


