class optimalChange:

    def optimalChange(self):
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






    print("will give best thing to improve")


