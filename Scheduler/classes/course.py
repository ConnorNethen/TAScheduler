from Scheduler.models import Course


class AppCourse:
    courseID = None
    name = None
    semester = None
    year = None

    def __init__(self, cid="", n="", s="", y=""):
        #courseExists = False
        if not isinstance(cid, str) or not isinstance(n, str) or not isinstance(s, str) or not isinstance(y, int):
            raise TypeError

        if not cid.isalnum():
            raise ValueError

        try:
            myCourseID = Course.objects.get(courseID=cid)
            #courseExists = True
        except:
            # check semester
            semesterExists = False
            for i in range(len(Course.SEMESTER_CHOICES)):
                if s == Course.SEMESTER_CHOICES[i][0]:
                    semesterExists = True
            if not semesterExists:
                raise ValueError

            # check year
            if y < 2020 or y > 2100:
                raise ValueError
            myCourse = Course(courseID=myCourseID, name=n, semester=s, year=y)
            myCourse.save()

        self.courseID = myCourse.courseID
        self.name = myCourse.name
        self.semester = myCourse.semester
        self.year = myCourse.year

    def getCourseID(self):
        return self.courseID

    def getName(self):
        return self.name

    def getSemester(self):
        return self.semester

    def getYear(self):
        return self.year

    def setName(self, n):
        if not isinstance(n, str):
            raise TypeError
        self.name = n
        self.save()

    def setSemester(self, s):
        if not isinstance(s, str):
            raise TypeError
        # if s is one of the SEMESTER_CHOICES ...
        semesterExists = False
        for i in range(len(Course.SEMESTER_CHOICES)):
            if s == Course.SEMESTER_CHOICES[i][0]:
                semesterExists = True
        if not semesterExists:
            raise ValueError

        self.semester = s
        self.save()

    def setYear(self, y):
        if not isinstance(y, int):
            raise TypeError
        # check year
        if y < 2020 or y > 2100:
            raise ValueError

        self.year = y
        self.save()

    def getUsers(self, cid):
        pass

    def addSection(self, sid):
        pass

    def getSections(self, cid):
        pass

    def removeCourse(self, cid):
        pass
