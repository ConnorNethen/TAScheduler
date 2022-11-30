import Scheduler.models
from classes.course import Course
import unittest


class TestCreate(unittest.TestCase):

    def test_SuccessfulCreate(self):
        Course.createCourse("CS361", "Fall", "2022")
        course361 = Course.objects.get(number="CS361")
        self.assertEqual(course361.number, "CS361", msg="Course Number not correct")
        self.assertEqual(course361.semester, "Fall", msg="Semester not correct")
        self.assertEqual(course361.year, "2022", msg="Year not correct")

    def test_InvalidArg(self):
        with self.assertRaises(TypeError, msg="wrong Arg Type"):
            Course.createCourse(Course, "Fall", "2022")
#test invalid argument in each parameter
    def test_OneArg(self):
        with self.assertRaises(TypeError, msg="not enough Arg"):
            Course.createCourse("CS361")

    def test_TwoArg(self):
        with self.assertRaises(TypeError, msg="not enough Arg"):
            Course.createCourse("CS361", "2022")

    def test_InvalidName(self):
        Course.createCourse("CS361", "Fall", "2022")
        with self.assertRaises(KeyError, msg="Key(Course) already exists"):
            Course.createCourse("CS361",  "Fall", "2022")
#test no args
#test 4 arga
#test number in wrong format, i.e. more than or less than 2 letters
# also more than or les than 3 numbers
#test if semster isnt fall,spring,summer,winter
#test year if year<2000? or >2040? year is a number?

class TestEditCourse(unittest.TestCase):

    def setUp(self):
        Scheduler.models.Course(number="CS361", semester="Fall", year="2022")

    def test_SuccessfulEdit(self):
        Course.editCourse("CS458", "Spring", "2023")
        course458 = Course.objects.get(number="CS458")
        self.assertEqual(course458.number, "CS458", msg="Course Number not updated correctly")
        self.assertEqual(course458.semester, "Spring", msg="Semester not updated correctly")
        self.assertEqual(course458.year, "2023", msg="Year not updated correctly")
#how is the course choosen to edit?
    def test_NullEdit(self):
        Course.editCourse(None, None, None)
        course361 = Course.objects.get(number="CS361")
        self.assertEqual(course361.number, "CS361", msg="Course Number should not have updated to None")
        self.assertEqual(course361.semester, "Fall", msg="Semester should not have updated to None")
        self.assertEqual(course361.year, "2022", msg="Year should not have updated to None")
#test none, in one of three parameters
#test none in two args
    def test_InvalidArg(self):
        with self.assertRaises(TypeError, msg="wrong Arg Type"):
            Course.editCourse(Course, "Fall", "2022")
#test invalid argument for each parameter
    def test_OneArg(self):
        with self.assertRaises(TypeError, msg="not enough Arg"):
            Course.editCourse("CS361")

    def test_TwoArg(self):
        with self.assertRaises(TypeError, msg="not enough Arg"):
            Course.editCourse("CS361", "2022")

    def test_InvalidName(self):
        with self.assertRaises(KeyError, msg="Key(Course) already exists"):
            Course.editCourse("CS361", "Fall", "2022")

#test no args
#test 4 args


