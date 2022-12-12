from django.test import TestCase
from Scheduler.classes.course import AppCourse
from Scheduler.models import Course, UserCourse, Section
from Scheduler.classes import app_user, course, section


class CourseCreationTests(TestCase):
    def test_Init(self):
        myCourse = AppCourse("CS361", "Introduction to Software Engineering", "F", 2022)
        self.assertEqual(myCourse.CourseID, Course.objects.get(courseID="CS361").courseID, msg= "Error")
        self.assertEqual(myCourse.name, Course.objects.get(name="Introduction to Software Engineering"))
        self.assertEqual(myCourse.semester, Course.objects.get(semster="F"))
        self.assertEqual(myCourse.year, Course.objects.get(year=2022))

    def test_No_Arguments(self):
        with self.assertRaises(TypeError, msg="Not Enough Arguments Given"):
            Course01 = AppCourse()

    def test_One_Argument(self):
        with self.assertRaises(TypeError, msg="Not Enough Arguments Given"):
            Course01 = AppCourse("CS361")

    def test_Two_Arguments(self):
        with self.assertRaises(TypeError, msg="Not Enough Arguments Given"):
            Course01 = AppCourse("CS361", "Introduction to Software Engineering")

    def test_Three_Arguments(self):
        with self.assertRaises(TypeError, msg="Not Enough Arguments Given"):
            Course01 = AppCourse("CS361", "Introduction to Software Engineering", "F")

    def test_More_Arguments(self):
        with self.assertRaises(TypeError, msg="Too Many Arguments Given"):
            Course01 = AppCourse("CS361", "Introduction to Software Engineering", "F", 2022, "Something")

    def test_Invalid_Id_Type(self):
        with self.assertRaises(TypeError, msg="Invalid CourseID Argument"):
            CourseA = AppCourse(361, "Introduction to Software Engineering", "F", 2022)

    def test_Invalid_Id_Value(self):
        with self.assertRaises(ValueError, msg="Invalid CourseID Argument"):
            CourseA = AppCourse("CS361.5", "Introduction to Software Engineering", "F", 2022)

    def test_Repeated_Id(self):
        Course01 = AppCourse("CS361", "Intro", "F", 2022)
        with self.assertRaises(TypeError, msg="CourseID is Not Unique"):
            Course02 = AppCourse("CS361", "Systems Programing", "F", 2022)


class CourseGetTests(TestCase):
    def setup(self):
        self.Course01 = AppCourse("CS361", "Introduction to Software Engineering", "F", 2022)
        self.Course01.save()

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
    def setup(self):
        self.Course01 = AppCourse("CS361", "Introduction to Software Engineering", "F", 2022)
        self.Course01.save()

    def test_setName(self):
        self.Course01.setName("Conclusion of Software Engineering")
        self.Course01.save()
        self.assertEqual(Course.objects.get(CourseID="CS361").name, "Conclusion of Software Engineering")

    def test_setName_NoArgs(self):
        with self.assertRaises(TypeError, msg="No arguments passed into function"):
            self.Course01.setName()

    def test_setName_ManyArgs(self):
        with self.assertRaises(TypeError, msg="Too many arguments passed into function"):
            self.Course01.setName("Introduction", "to Software Engineering")

    def test_setSemester(self):
        self.Course01.setSemester("U")
        self.Course01.save()
        self.assertEqual(Course.objects.get(CourseID="CS361").semester, "U")

    def test_setSemester_NoArgs(self):
        with self.assertRaises(TypeError, msg="No arguments passed into function"):
            self.Course01.setSemester()

    def test_setSemester_ManyArgs(self):
        with self.assertRaises(TypeError, msg="Too many arguments passed into function"):
            self.Course01.setSemester("F", "S")

    def test_setYear(self):
        self.Course01.setYear(2025)
        self.Course01.save()
        self.assertEqual(Course.objects.get(CourseID="CS361").year, 2025)

    def test_setYear_NoArgs(self):
        with self.assertRaises(TypeError, msg="No arguments passed into function"):
            self.Course01.setYear()

    def test_setYear_ManyArgs(self):
        with self.assertRaises(TypeError, msg="Too many arguments passed into function"):
            self.Course01.setYear(2022, 2023)


class TestGetUsers(TestCase):
    def setUp(self):
        # create users
        user01 = app_user("123", "user01@test.com", "pass")
        user01.save()
        user02 = app_user("456", "user02@test.com", "pass")
        user02.save()
        user03 = app_user("789", "user03@test.com", "pass")
        user03.save()

        # create courses
        self.Course01 = AppCourse(courseID="CS 361", name="Intro to SE", semester="F", year=2022)
        self.Course01.save()

        # create connections
        a = UserCourse(user="123", course="CS 361")
        a.save()
        b = UserCourse(user="456", course="CS 361")
        b.save()
        c = UserCourse(user="789", course="CS 361")
        c.save()

    def test_successful_call(self):
        listOfUsers = self.Course01.getUsers()
        self.assertIsInstance(listOfUsers[0], app_user, msg="Error creating instance")
        self.assertEqual(listOfUsers[0].pID, "123")
        self.assertIsInstance(listOfUsers[1], app_user, msg="Error creating instance")
        self.assertEqual(listOfUsers[1].pID, "456")
        self.assertIsInstance(listOfUsers[0], app_user, msg="Error creating instance")
        self.assertEqual(listOfUsers[2].pID, "789")

    def test_invalid_course(self):
        with self.assertRaises(TypeError, msg="Course does not exist"):
            listOfUsers = self.Course02.getUsers()


class TestGetSection(TestCase):
    def setup(self):
        pass


class TestSetSection(TestCase):
    def setup(self):
        pass


class TestRemoveCourse(TestCase):
    def setup(self):
        self.Course01 = AppCourse(courseID="CS 361", name="Intro to SE", semester="F", year=2022)
        self.Course02 = AppCourse(courseID="CS 337", name="Systems Programming", semester="F", year=2022)



#class CourseCreationTests(TestCase):
#    def test_course_creation(self):
#        course = Course.objects.create(
#            courseID='CS361',
#            name='Introduction to Software Engineering',
#           semester='F',
#            year=2022
#        )
#        self.assertEqual(course.courseID, 'CS361')
#        self.assertEqual(course.name, 'Introduction to Software Engineering')
#        self.assertEqual(course.semester, 'F')
#        self.assertEqual(course.year, 2022)
#
#
#class CourseDeletionTests(TestCase):
#    def setUp(self) -> None:
#        self.course = Course.objects.create(
#            courseID='CS361',
#            name='Introduction to Software Engineering',
#            semester='F',
#            year=2022
#        )
#
#    def test_course_deletion_success(self):
#        self.course.delete()
#        self.assertEqual(Course.objects.count(), 0, msg='Course was not deleted')
#
#    def test_course_deletion_success_by_id(self):
#        Course.objects.filter(courseID='CS361').delete()
#        self.assertEqual(Course.objects.count(), 0, msg='Course was not deleted')
#
#    def test_course_deletion_failure_by_id(self):
#        Course.objects.filter(courseID='CS362').delete()
#        self.assertEqual(Course.objects.count(), 1, msg='Course was deleted')
#
#
#class CourseUpdateTests(TestCase):
#    def setUp(self) -> None:
#        self.course = Course.objects.create(
#            courseID='CS361',
#            name='Introduction to Software Engineering',
#            semester='F',
#            year=2022
#        )
#
#    def test_course_update_success_id(self):
#        self.course.courseID = 'CS362'
#        self.course.save()
#        self.assertEqual(self.course.courseID, 'CS362', msg='Course ID was not updated')
#
#    def test_course_update_success_name(self):
#        self.course.name = 'Introduction to Software Engineering II'
#        self.course.save()
#        self.assertEqual(self.course.name, 'Introduction to Software Engineering II',
#                         msg='Course name was not updated')
#
#    def test_course_update_success_semester(self):
#        self.course.semester = 'S'
#        self.course.save()
#        self.assertEqual(self.course.semester, 'S', msg='Course semester was not updated')
#
#    def test_course_update_success_year(self):
#        self.course.year = 2023
#        self.course.save()
#        self.assertEqual(self.course.year, 2023, msg='Course year was not updated')
#
#    def test_course_update_failure_id(self):
#        self.course.courseID = ''
#        self.course.save()
#        self.assertEqual(self.course.courseID, 'CS361', msg='Course ID was updated')
#        self.course.courseID = None
#        self.course.save()
#        self.assertEqual(self.course.courseID, 'CS361', msg='Course ID was updated')
#
#    def test_course_update_failure_name(self):
#        self.course.name = ''
#        self.course.save()
#        self.assertEqual(self.course.name, 'Introduction to Software Engineering',
#                         msg='Course name was updated')
#        self.course.name = None
#        self.course.save()
#        self.assertEqual(self.course.name, 'Introduction to Software Engineering',
#                         msg='Course name was updated')
#
#    def test_course_update_failure_semester(self):
#        self.course.semester = ''
#        self.course.save()
#        self.assertEqual(self.course.semester, 'F', msg='Course semester was updated')
#        self.course.semester = None
#        self.course.save()
#        self.assertEqual(self.course.semester, 'F', msg='Course semester was updated')
#
#    def test_course_update_failure_year(self):
#        self.course.year = ''
#        self.course.save()
#        self.assertEqual(self.course.year, 2022, msg='Course year was updated')
#        self.course.year = None
#        self.course.save()
#        self.assertEqual(self.course.year, 2022, msg='Course year was updated')
