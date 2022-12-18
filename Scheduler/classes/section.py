import Scheduler.models
from Scheduler.models import Course, Section, AppUser


class AppSection:
    sectionID = None
    courseID = None
    userPID = None

    def __init__(self, section="", course=""):
        noUser = True
        if not isinstance(section, str) or not isinstance(course, str):
            raise TypeError
        try:
            myCourse = Course.objects.get(courseID=course)
        except Scheduler.models.Course.DoesNotExist:
            raise TypeError
        try:
            mySection = Section.objects.get(courseID=myCourse, sectionID=section)
            if mySection.user is not None: noUser = False
        except Scheduler.models.Section.DoesNotExist:
            mySection = Section(courseID=myCourse, sectionID=section)
            mySection.save()
        if noUser:
            self.userPID = ""
        else:
            self.userPID = mySection.user.pID

        self.sectionID = mySection.sectionID
        self.courseID = mySection.courseID.courseID
