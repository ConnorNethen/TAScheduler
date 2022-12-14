from Scheduler.classes.app_user import AppUserClass
from Scheduler.models import Course, Section, AppUser


class AppSection:
    sectionID = None
    courseID = None
    userPID = None

    def __init__(self, section="", course=""):
        noUser = True
        if not isinstance(section, str) or not isinstance(course, str):
            return TypeError
        try :
            myCourse = Course.objects.get(courseID= course)
        except Exception:
            return TypeError
        try:
            mySection = Section.objects.get(courseID=myCourse, sectionID=section)
            if mySection.user is not None: noUser = False
        except Exception:
            mySection = Section(courseID= myCourse, sectionID=section)
            mySection.save()
        if noUser: self.userPID = ""
        else: self.userPID = mySection.user.pID

        self.sectionID = mySection.sectionID
        self.courseID = mySection.courseID.courseID


    def getSectionID(self):
        return self.sectionID

    def getCourseID(self):
        return self.courseID

    def getUser(self):
        if self.userPID == "":
            return None
        else:
            return AppUserClass(self.userPID)

    def setUser(self, user = ""):
        if user == "" or not isinstance(user, str):
            raise TypeError
        try:
            myUser = AppUser.objects.get(pID= user)
            myCourse = Course.objects.get(courseID= self.courseID)
        except Exception:
            return TypeError

        mySection = Section.objects.get(courseID= myCourse, sectionID= self.sectionID)
        mySection.user = myUser
        mySection.save()
        self.userPID = user
        return