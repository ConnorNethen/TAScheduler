from Scheduler.models import Course


class AppCourse():
    courseID = None
    name = None
    semester = None
    year = None

    def __init__(self, cid=None, n=None, s=None, y=None):
        repeatedID = False
        if not isinstance(cid, str) or not isinstance(n, str) or not isinstance(s, str) or not isinstance(y, int):
            raise TypeError

        if not cid.isalnum():
            raise ValueError

        try:
            myCourseID = Course.objects.get(courseID=cid)
        except Exception:
            raise TypeError

        try:
            myName = Course.objects.get(name=n)
        except Exception:
            raise TypeError

        try:
            mySemester = Course.objects.get(semester=s)
        except Exception:
            raise TypeError

        try:
            myYear = Course.objects.get(year=y)
        except Exception:
            raise TypeError

        self.courseID = myCourseID
        self.name = myName
        self.semester = mySemester
        self.year = myYear

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

    def setSemester(self, s):
        if not isinstance(s, str):
            raise TypeError
        # if s is one of the SEMESTER_CHOICES ...

        self.semester = s

    def setYear(self, y):
        if not isinstance(y, int):
            raise TypeError
        self.year = y

    def getUsers(self, courseID):
        pass

    def addSection(self, sectionID):
        pass

    def getSections(self, courseID):
        pass

    def removeCourse(self, courseID):
        pass
