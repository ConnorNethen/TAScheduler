import Scheduler
from Scheduler.models import Course, UserCourse, AppUser
from Scheduler.classes import app_user


class AppCourse:
    courseID = None
    name = None
    semester = None
    year = None

    def __init__(self, cid="", n="", s="", y=""):
        if not isinstance(cid, str) or not isinstance(n, str) or not isinstance(s, str) or not isinstance(y, int):
            raise TypeError

        if cid is not None:
            if not cid.isalnum():
                raise ValueError

        try:
            myCourse = Course.objects.get(courseID=cid)
        except Scheduler.models.Course.DoesNotExist:
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
            myCourse = Course(courseID=cid, name=n, semester=s, year=y)
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
        try:
            myCourse = Course.objects.get(courseID=self.courseID)
        except Exception:
            raise TypeError
        myCourse.name = n
        myCourse.save()
        self.name = myCourse.name

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
        try:
            myCourse = Course.objects.get(courseID=self.courseID)
        except Exception:
            raise TypeError
        myCourse.semester = s
        myCourse.save()
        self.semester = myCourse.semester

    def setYear(self, y):
        if not isinstance(y, int):
            raise TypeError
        # check year
        if y < 2020 or y > 2100:
            raise ValueError
        try:
            myCourse = Course.objects.get(courseID=self.courseID)
        except Exception:
            raise TypeError
        myCourse.year = y
        myCourse.save()
        self.year = myCourse.year

    def getUsers(self, cid):
        if not isinstance(str, cid):
            raise TypeError
        listToReturn = []
        try:
            myCourse = Course.objects.get(courseID=cid)
            listOfUserCourse = UserCourse.objects.filter(course=myCourse)
            for i in len(listOfUserCourse):
                # listToReturn.append(i.user)
                listToReturn.append(listOfUserCourse[i])
        except Scheduler.models.Course.DoesNotExist:
            raise ValueError




    def addSection(self, sid):
        pass

    def getSections(self, cid):
        pass

    def removeCourse(self, cid):
        if not isinstance(str, cid):
            raise TypeError
        try:
            myCourse = Course.objects.get(courseID=self.courseID) # course found
            # change course attributes to None (delete the course)
            self.courseID = None
            self.name = None
            self.semester = None
            self.year = None
        except Exception: # course not found
            raise TypeError("Course does not exist, unable to delete")




