import string
import Scheduler
from Scheduler.classes.section import AppSection
from Scheduler.models import Course, UserCourse, Section


class AppCourse:
    courseID = None
    name = None
    semester = None
    year = None

    def __init__(self, cid="", n="", s="", y=""):
        if not isinstance(cid, str) or not isinstance(n, str) or not isinstance(s, str) or not isinstance(y, int):
            raise TypeError

        if cid == "":
            raise TypeError

        punctList = string.punctuation
        for i in cid:
            if i in punctList:
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

    def getUsers(self):
        listToReturn = []
        try:
            myCourse = Course.objects.get(courseID=self.courseID)
            listOfUserCourse = UserCourse.objects.filter(course=myCourse)
            for i in listOfUserCourse:
                listToReturn.append(i.user.pID)
        except Exception:
            raise ValueError

        return listToReturn

    def addSection(self, sid):
        if not isinstance(sid, str):
            raise TypeError
        if len(sid) > 3:
            raise ValueError

        try:
            myCourse = Course.objects.get(courseID=self.courseID)
            Section.objects.get(courseID=myCourse, sectionID=sid)
        except Exception:
            AppSection(sid,self.courseID)
            return
        raise TypeError("Section Exists")

    def getSections(self):
        listToReturn = []
        try:
            myCourse = Course.objects.get(courseID=self.courseID)
            listOfSections = Section.objects.filter(course=myCourse)
        except Exception:
            return []
        for i in listOfSections:
            listToReturn.append(AppSection(i.sectionID,self.courseID))
        return listToReturn

    def removeCourse(self):
        try:
            courseToDelete = Course.objects.get(courseID=self.courseID)
            Course.objects.filter(courseID=self.courseID).delete()
        except Scheduler.models.Course.DoesNotExist:
            raise ValueError("course does not exist")

    def removeSection(self, sid):
        if not isinstance(sid, str):
            raise TypeError
        try:
            Section.objects.get(sectionID=sid).delete()
        except Exception:
            raise ValueError("section does not exist")
