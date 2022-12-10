from django.test import TestCase
from Scheduler.models import Course
from Scheduler.classes import app_user


class CourseCreationTests(TestCase):
    def test_Init(self):
        Course361 = Course("CS361", "Introduction to Software Engineering", "F", 2022)
        Course361.save()
        self.assertTrue(Course.objects.filter(CourseID="CS361").exists())

    def test_No_Arguments(self):
        with self.assertRaises(ValueError, msg="Not Enough Arguments Given"):
            Course01 = Course()

    def test_One_Argument(self):
        with self.assertRaises(ValueError, msg="Not Enough Arguments Given"):
            Course01 = Course("CS361")

    def test_Two_Arguments(self):
        with self.assertRaises(ValueError, msg="Not Enough Arguments Given"):
            Course01 = Course("CS361", "Introduction to Software Engineering")

    def test_Three_Arguments(self):
        with self.assertRaises(ValueError, msg="Not Enough Arguments Given"):
            Course01 = Course("CS361", "Introduction to Software Engineering", "F")

    def test_More_Arguments(self):
        with self.assertRaises(ValueError, msg="Too Many Arguments Given"):
            Course01 = Course("CS361", "Introduction to Software Engineering", "F", 2022, "Something")

    def test_Invalid_Id_Type(self):
        with self.assertRaises(ValueError, msg="Invalid CourseID Argument"):
            CourseA = Course(361, "Introduction to Software Engineering", "F", 2022)

    def test_Invalid_Id_Value(self):
        with self.assertRaises(TypeError, msg="Invalid CourseID Argument"):
            CourseA = Course("CS361.5", "Introduction to Software Engineering", "F", 2022)

    def test_Repeated_Id(self):
        Course01 = Course("CS361", "Intro", "F", 2022)
        with self.assertRaises(ValueError, msg="CourseID is Not Unique"):
            Course02 = Course("CS361", "Systems Programing", "F", 2022)


class CourseGetTests(TestCase):
    def setup(self):
        self.Course01 = Course("CS361", "Introduction to Software Engineering", "F", 2022)
        self.Course01.save()
        self.Course02 = Course("CS337", "Systems Programming", "S", 2023)
        self.Course02.save()

    def test_getCourseID(self):
        self.assertEqual(self.Course01.getCourseID(), "CS361")
        self.assertEqual(self.Course02.getCourseID(), "CS337")

    def test_getName(self):
        self.assertEqual(self.Course01.getName(), "Introduction to Software Engineering")
        self.assertEqual(self.Course02.getName(), "Systems Programming")

    def test_getSemester(self):
        self.assertEqual(self.Course01.getSemester(), "F")
        self.assertEqual(self.Course02.getSemester(), "S")

    def test_getYear(self):
        self.assertEqual(self.Course01.getYear(), 2022)
        self.assertEqual(self.Course02.getYear(), 2023)


class CourseSetTests(TestCase):
    def setup(self):
        self.Course01 = Course("CS361", "Introduction to Software Engineering", "F", 2022)
        self.Course01.save()
        self.Course02 = Course("CS337", "Systems Programming", "S", 2023)
        self.Course02.save()

    def test_setName(self):
        self.Course01.setName("Conclusion of Software Engineering")
        self.Course02.setName("Computer Programming")
        self.assertEqual(Course.objects.get(CourseID="CS361").name, "Conclusion of Software Engineering")
        self.assertEqual(Course.objects.get(CourseID="CS337").name, "Computer Programming")

    def test_setSemester(self):
        self.Course01.setSemester("U")
        self.Course01.save()
        self.Course02.setSemester("W")
        self.Course02.save()
        self.assertEqual(Course.objects.get(CourseID="CS361").semester, "U")
        self.assertEqual(Course.objects.get(CourseID="CS337").semester, "W")

    def test_setYear(self):
        self.Course01.setYear(2025)
        self.Course01.save()
        self.Course02.setYear(2025)
        self.Course02.save()
        self.assertEqual(Course.objects.get(CourseID="CS361").year, 2025)
        self.assertEqual(Course.objects.get(CourseID="CS337").year, 2025)


class TestGetUsers(TestCase):
    def setUp(self):
        # create a couple users
        self.user = app_user(123, "user@test.com", "pass")
        self.user2 = app_user(456, "user2@test.com", "pass")

        # create a couple courses
        Course01 = Course(courseID="CS 361 XX", name="Intro to SE", semester="F", year=2022)
        Course01.save()

        b = Course(courseID="CS 337 XX", name="System Programming", semester="F", year=2022)
        b.save()

        c = Course(courseID="CS 361 X", name="Intro to SE", semester="F", year=2022)
        c.save()



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