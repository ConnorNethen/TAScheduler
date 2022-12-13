
from django.test import TestCase

from Scheduler.classes.section import AppSection
from Scheduler.models import Section, Course, AppUser
from Scheduler.classes import section, app_user

class TestInitSection(TestCase):

    def setUp(self):
        testCourse = Course(courseID="CS 361 XX", name="Intro to SE", semester="F", year= 2022)
        testCourse.save()

        testSection = Section(courseID= "CS 361 XX", sectionID= "001")
        testSection.save()

    def test_sectionIDinDatabase(self):
        mySection = AppSection("001", "CS 361 XX")
        self.assertEqual(mySection.sectionID, "001", msg= "section ID doesn't equal 001")

    def test_courseIDinDatabase(self):
        mySection = AppSection("001", "CS 361 XX")
        self.assertEqual(mySection.courseID, "CS 361 XX", msg="section's course Id doesn't equal CS 361 XX")

    def test_sectionExistsInDatabase(self):
        AppSection("001", "CS 361 XX")
        self.assertEqual(Section.objects.all().count(), 1, msg= "section created when section existed in DB")

    def test_sectionDoesNotExistInDBSectionID(self):
        AppSection("002", "CS 361 XX")
        sectionList = Section.objects.filter(courseID= "CS 361 XX")
        inSectionList = False
        for i in sectionList:
            if i.sectionID == "002": inSectionList = True
        self.assertTrue(inSectionList, msg= "Section not created in database when no section exists.")

    def test_sectionDoseNotExistInDBcount(self):
        AppSection("002", "CS 361 XX")
        self.assertEqual(Section.objects.all().count(), 2, msg= "section not created when it doesn't existed in DB")

    def test_courseDoesNotExistInDatabase(self):
        with self.assertRaises(TypeError, msg="Type Error not raised when Course doesn't exist in the Database"):
            AppSection("001", "CS 241")

    def test_oneArgument(self):
        with self.assertRaises(TypeError, msg= "Exception not raised when one argument received"):
            AppSection("001")

    def test_threeArguments(self):
        with self.assertRaises(TypeError, msg= "Exception not raised when three arguments are received"):
            AppSection("001", "CS 361 XX", "thirdArg")

    def test_invalidFirstArgument(self):
        with self.assertRaises(TypeError, msg= "Exception not raised, when the first argument is an invalid type"):
            AppSection(123.456, "CS 361 XX")

    def test_invalidSecondArgument(self):
        with self.assertRaises(TypeError, msg= "Exception not raised, when the second argument is an invalid type"):
            AppSection("001", 123.456)

class TestGetSectionID(TestCase):
    def setUp(self):
        testCourse = Course(courseID="CS 361 XX", name="Intro to SE", semester="F", year=2022)
        testCourse.save()
        self.mySection = AppSection("001", "CS 361 XX")

    def test_sectionID(self):
        self.assertEqual(self.mySection.getSectionID(), "001", msg= "getSectionID() doesn't return correct section ID.")

    def test_oneArg(self):
        with self.assertRaises(TypeError, msg= "Type error not raised when argument is presented in getSectionID()."):
            self.mySection.getSectionID("oneArg")

class TestGetCourseID(TestCase):

    def setUp(self):
        testCourse = Course(courseID="CS 361 XX", name="Intro to SE", semester="F", year= 2022)
        testCourse.save()
        self.mySection = AppSection("001", "CS 361 XX")

    def test_courseID(self):
        self.assertEqual(self.mySection.getCourseID(), "CS 361 XX", msg= "getCourseID() didnt return CS 361 XX")

    def test_oneArg(self):
        with self.assertRaises(TypeError, msg= "Error not raised when an argument is presented in getCourseID()"):
            self.mySection.getCourseID("oneArg")

class TestGetUser(TestCase):

    def setUp(self):
        user = AppUser("123", "user@test.com", "pass")
        user.save()

        testCourse = Course(courseID= "CS 361 XX", name= "Intro to SE", semester= "F", year= 2022)
        testCourse.save()

        userSec = Section(courseID= "CS 361 XX", sectionID= "001", user= "123")
        userSec.save()

    def test_userExistsInSection(self):
        mySection = section("001", "CS 361 XX")
        myUser = mySection.getUser()
        self.assertIsInstance(myUser, app_user, msg= "does not return instance of an app_user")

    def test_noUserInSection(self):
        mySection = section("002", "CS 361 XX")
        with self.assertIsNone(mySection.getUser, msg= "none not returned with no user in section")

    def test_oneArg(self):
        mySection = section("001", "CS 361 XX")
        with self.assertRaises(TypeError, msg= "Exception not raised, when an argument is placed"):
            mySection.getUser("oneArg")

class TestSetUser(TestCase):

    def setUp(self):
        user = AppUser("123", "user@test.com", "pass")
        user.save()
        user2 = AppUser("456", "user2@test.com", "pass")
        user2.save()

        testCourse = Course(courseID= "CS 361 XX", name= "Intro to SE", semester= "F", year= 2022)
        testCourse.save()

        userSec = Section(courseID= "CS 361 XX", sectionID= "001", user= "123")
        userSec.save()

    def test_NoUserInSection(self):
        mySection = AppSection("002", "CS 361 XX")
        mySection.setUser("123")
        sectionInDB = Section.objects.get(sectionID= "002", courseID= "CS 361 XX")
        self.assertEqual(sectionInDB.user, "123", msg= "user not updated for section in DB")

    def test_UserInSection(self):
        mySection = AppSection("001", "CS 361 XX")
        mySection.setUser("456")
        sectionInDB = Section.objects.get(sectionID= "001", courseID= "CS 361 XX")
        self.assertEqual(sectionInDB.user, "456", msg= "user not updated for section in DB")

    def test_UserNotInDatabaseAppSection(self):
        mySection = AppSection("001", "CS 361 XX")
        mySection.setUser("789")
        self.assertIsNone(mySection.userPID, msg= "None is not the sections user pid with no user assigned.")

    def test_UserNotInDatabaseDbCheck(self):
        mySection = AppSection("001", "CS 361 XX")
        mySection.setUser("789")
        sectionInDB = Section.objects.get(sectionID="001", courseID="CS 361 XX")
        self.assertIsNone(sectionInDB.user, msg= "None is not the sections user pid with no user assigned.")

    def test_invalidArgument(self):
        mySection = AppSection("001", "CS 361 XX")
        with self.assertRaises(TypeError, "Exception not raised with invalid argument type"):
            mySection.setUser(123.456)

    def test_noArgs(self):
        mySection = AppSection("001", "CS 361 XX")
        mySection.setUser()
        sectionInDB = Section.objects.get(sectionID= "001", courseID= "CS 361 XX")
        self.assertEqual(sectionInDB.user, "123", msg= "user not updated for section in DB")

    def test_twoArgs(self):
        mySection = AppSection("001", "CS 361 XX")
        with self.assertRaises(TypeError, msg= "Exception not raised when two arguments are presented."):
            mySection.setUser("123", "456")



