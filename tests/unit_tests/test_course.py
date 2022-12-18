from django.test import TestCase
from Scheduler.classes.course import AppCourse
from Scheduler.classes.section import AppSection
from Scheduler.models import Course, UserCourse, Section, AppUser
from Scheduler.classes import app_user


class CourseCreationTests(TestCase):
    def setUp(self):
        self.myCourse = AppCourse("CS361", "Introduction to Software Engineering", "F", 2022)

    def test_Init_CourseID(self):
        self.assertEqual(self.myCourse.courseID, Course.objects.get(courseID="CS361").courseID)

    def test_Init_Name(self):
        self.assertEqual(self.myCourse.name, Course.objects.get(courseID="CS361").name)

    def test_Init_Semester(self):
        self.assertEqual(self.myCourse.semester, Course.objects.get(courseID="CS361").semester)

    def test_Init_Year(self):
        self.assertEqual(self.myCourse.year, Course.objects.get(courseID="CS361").year)

    def test_No_Arguments(self):
        with self.assertRaises(TypeError, msg="Not Enough Arguments Given"):
            self.Course01 = AppCourse()

    def test_One_Argument(self):
        with self.assertRaises(TypeError, msg="Not Enough Arguments Given"):
            self.Course01 = AppCourse("CS361")

    def test_Two_Arguments(self):
        with self.assertRaises(TypeError, msg="Not Enough Arguments Given"):
            self.Course01 = AppCourse("CS361", "Introduction to Software Engineering")

    def test_Three_Arguments(self):
        with self.assertRaises(TypeError, msg="Not Enough Arguments Given"):
            self.Course01 = AppCourse("CS361", "Introduction to Software Engineering", "F")

    def test_More_Arguments(self):
        with self.assertRaises(TypeError, msg="Too Many Arguments Given"):
            self.Course01 = AppCourse("CS361", "Introduction to Software Engineering", "F", 2022, "Something")

    def test_Invalid_Id_Type(self):
        with self.assertRaises(TypeError, msg="Invalid CourseID Argument"):
            self.CourseA = AppCourse(361, "Introduction to Software Engineering", "F", 2022)

    def test_Invalid_Id_Value(self):
        with self.assertRaises(ValueError, msg="Invalid CourseID Argument"):
            self.CourseA = AppCourse("CS361.5", "Introduction to Software Engineering", "F", 2022)

    def test_Invalid_Name_Type(self):
        with self.assertRaises(TypeError, msg="Name is of Invalid Type"):
            self.Course01 = AppCourse("CS345", 123, "F", 2022)

    def test_Invalid_Semester_Type(self):
        with self.assertRaises(TypeError, msg="Semester is of Invalid Type"):
            self.Course01 = AppCourse("CS345", "Intro", 123, 2022)

    def test_Invalid_Semester_Value(self):
        with self.assertRaises(ValueError, msg="Semester is an Invalid Value"):
            self.Course01 = AppCourse("CS345", "Intro", "Q", 2022)

    def test_Invalid_Year_Type(self):
        with self.assertRaises(TypeError, msg="Year is of Invalid Type"):
            self.Course01 = AppCourse("CS345", "Intro", "F", "2022")

    def test_Invalid_Year_Value(self):
        with self.assertRaises(ValueError, msg="Year is an Invalid Value"):
            self.Course01 = AppCourse("CS345", "Intro", "F", 1500)


class CourseGetTests(TestCase):
    def setUp(self):
        self.Course01 = AppCourse("CS361", "Introduction to Software Engineering", "F", 2022)

    def test_getCourseID(self):
        self.assertEqual(self.Course01.getCourseID(), "CS361")

    def test_getCourseID_ManyArg(self):
        with self.assertRaises(TypeError, msg="Too many arguments passed into function"):
            self.Course01.getCourseID("CS361")

    def test_getName(self):
        self.assertEqual(self.Course01.getName(), "Introduction to Software Engineering")

    def test_getName_ManyArg(self):
        with self.assertRaises(TypeError, msg="Too many arguments passed into function"):
            self.Course01.getName("Systems Programming")

    def test_getSemester(self):
        self.assertEqual(self.Course01.getSemester(), "F")

    def test_getSemester_ManyArg(self):
        with self.assertRaises(TypeError, msg="Too many arguments passed into function"):
            self.Course01.getSemester("U")

    def test_getYear(self):
        self.assertEqual(self.Course01.getYear(), 2022)

    def test_getYear_ManyArg(self):
        with self.assertRaises(TypeError, msg="Too many arguments passed into function"):
            self.Course01.getYear(2022)


class CourseSetTests(TestCase):
    def setUp(self):
        self.Course01 = AppCourse("CS361", "Introduction to Software Engineering", "F", 2022)

    def test_setName(self):
        self.Course01.setName("Conclusion of Software Engineering")
        self.assertEqual(Course.objects.get(courseID="CS361").name, "Conclusion of Software Engineering")

    def test_setName_NoArgs(self):
        with self.assertRaises(TypeError, msg="No arguments passed into function"):
            self.Course01.setName()

    def test_setName_ManyArgs(self):
        with self.assertRaises(TypeError, msg="Too many arguments passed into function"):
            self.Course01.setName("Introduction", "to Software Engineering")

    def test_setSemester(self):
        self.Course01.setSemester("U")
        self.assertEqual(Course.objects.get(courseID="CS361").semester, "U")

    def test_setSemester_NoArgs(self):
        with self.assertRaises(TypeError, msg="No arguments passed into function"):
            self.Course01.setSemester()

    def test_setSemester_ManyArgs(self):
        with self.assertRaises(TypeError, msg="Too many arguments passed into function"):
            self.Course01.setSemester("F", "S")

    def test_setYear(self):
        self.Course01.setYear(2025)
        self.assertEqual(Course.objects.get(courseID="CS361").year, 2025)

    def test_setYear_NoArgs(self):
        with self.assertRaises(TypeError, msg="No arguments passed into function"):
            self.Course01.setYear()

    def test_setYear_ManyArgs(self):
        with self.assertRaises(TypeError, msg="Too many arguments passed into function"):
            self.Course01.setYear(2022, 2023)


class TestGetUsers(TestCase):
    def setUp(self):
        # create users
        user01 = AppUser(pID="123", email="user01@test.com", password="pass")
        user01.save()
        user02 = AppUser(pID="456", email="user02@test.com", password="pass")
        user02.save()
        user03 = AppUser(pID="789", email="user03@test.com", password="pass")
        user03.save()

        self.Course01 = AppCourse("CS 361", "Intro to SE", "F", 2022)
        self.Course02 = AppCourse("CS 337", "Systems", "F", 2022)
        a = Course.objects.get(courseID=self.Course01.getCourseID())

        # create connections
        a1 = UserCourse(user=user01, course=a)
        a1.save()
        b1 = UserCourse(user=user02, course=a)
        b1.save()
        c1 = UserCourse(user=user03, course=a)
        c1.save()

    def test_successful_call(self):
        listOfUsers = self.Course01.getUsers()
        self.assertEqual(listOfUsers[0], "123")
        self.assertEqual(listOfUsers[1], "456")
        self.assertEqual(listOfUsers[2], "789")

    def test_empty_list(self):
        listOfUsers = self.Course02.getUsers()
        self.assertFalse(bool(listOfUsers), msg="list is not empty")

    def test_getUsers_many_arg(self):
        with self.assertRaises(TypeError, msg="too many arguments given in function"):
            self.listOfUsers = self.Course01.getUsers("CS 361")



class TestAddSection(TestCase):
    def setUp(self):
        # create a course
        self.Course01 = AppCourse("CS 361", "Intro to SE", "F", 2022)

    def test_addSection(self):
        self.Course01.addSection("001")
        myCourse = Course.objects.get(courseID="CS 361")
        self.assertEqual(Section.objects.filter(courseID= myCourse).count(), 1, msg="section not added")

    def test_repeated_addSection(self):
        self.Course01.addSection("001")
        with self.assertRaises(TypeError, msg="section for this course already exists"):
            self.Course01.addSection("001")

    def test_invalidSection_Type(self):
        with self.assertRaises(ValueError, msg="section id is invalid"):
            self.Course01.addSection("1001")

    def test_invalidSection_Value(self):
        with self.assertRaises(TypeError, msg="section id is invalid"):
            self.Course01.addSection(123)

    def test_addSection_no_arg(self):
        with self.assertRaises(TypeError, msg="no arguments given in function"):
            self.Course01.addSection()

    def test_addSection_many_arg(self):
        with self.assertRaises(TypeError, msg="too many arguments given in function"):
            self.Course01.addSection("001", "002")


class TestGetSections(TestCase):
    def setUp(self):
        # create a course
        self.Course01 = AppCourse("CS 361", "Intro to SE", "F", 2022)
        self.Course02 = AppCourse("CS 337", "Systems", "F", 2022)

        # create sections
        #self.Course01.addSection("001")
        #self.Course01.addSection("002")
        #self.Course01.addSection("003")
        a = Course.objects.get(courseID="CS 361")

        # create connections
        a1 = Section(sectionID="001", courseID=a)
        a1.save()
        b1 = Section(sectionID="002", courseID=a)
        b1.save()
        c1 = Section(sectionID="003", courseID=a)
        c1.save()

    def test_successful_call(self):
        listOfSections = self.Course01.getSections()
        for i in listOfSections:
            self.assertIsInstance(i, AppSection, msg="not an instance of appSection")
            self.assertEqual(i.courseID, "001" or "002" or "003", msg= "Section returned not in Course")
    def test_empty_list(self):
        listOfSections = self.Course02.getSections()
        self.assertFalse(bool(listOfSections), msg="list is not empty")

    def test_invalid_course(self):
        with self.assertRaises(TypeError, msg="Course does not exist"):
            self.listOfSections = self.Course01.getSections("CS 250")

    def test_invalid_course_Type(self):
        with self.assertRaises(TypeError, msg="invalid argument passed into function"):
            self.listOfSections = self.Course01.getSections(123)


    def test_getUsers_many_arg(self):
        with self.assertRaises(TypeError, msg="too many arguments given in function"):
            self.listOfSections = self.Course01.getSections("CS 361", "CS 337")


class TestRemoveCourse(TestCase):
    def setUp(self):
        self.Course01 = AppCourse("CS 361", "Intro to SE", "F", 2022)
        self.Course02 = AppCourse("CS 337", "Systems Programming", "F", 2022)

    def test_successful_remove(self):
        self.Course01.removeCourse()
        self.assertEqual(Course.objects.all().count(), 1, msg="course not removed")
        self.Course02.removeCourse()
        self.assertEqual(Course.objects.all().count(), 0, msg="course not removed")

    def test_repeated_remove(self):
        self.Course01.removeCourse()
        self.Course01.removeCourse()
        self.assertEqual(Course.objects.all().count(), 1, msg="course was removed when it should not have")

    def test_remove_many_arg(self):
        with self.assertRaises(TypeError, msg="too many arguments given in function"):
            self.Course01.removeCourse("CS 361")



