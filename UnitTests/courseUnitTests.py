import Scheduler.models
from classes.course import Course
import unittest


class TestCreate(unittest.TestCase):

    def test_SuccessfulCreate(self):
        Course.createCourse("CS361", "Fall", 2022)
        course361 = Course.objects.get(number="CS361")
        self.assertEqual(course361.number, "CS361", msg="Course Number not correct")
        self.assertEqual(course361.semester, "Fall", msg="Semester not correct")
        self.assertEqual(course361.year, 2022, msg="Year not correct")

    def test_InvalidArg(self):
        with self.assertRaises(TypeError, msg="wrong Arg Type"):
            Course.createCourse(Course, "Fall", 2022)

    def test_NoArg(self):
        with self.assertRaises(TypeError, msg="not enough Type"):
            Course.createCourse()

    def test_OneArg(self):
        with self.assertRaises(TypeError, msg="not enough Arg"):
            Course.createCourse("CS361")

    def test_TwoArg(self):
        with self.assertRaises(TypeError, msg="not enough Arg"):
            Course.createCourse("CS361", 2022)

    def test_FourArg(self):
        with self.assertRaises(TypeError, msg="too many Arg"):
            Course.createCourse("CS361", "Fall", 2022, "Tuesday 2:30",)

    def test_InvalidName(self):
        Course.createCourse("CS361", "Fall", 2022)
        with self.assertRaises(KeyError, msg="Key(Course) already exists"):
            Course.createCourse("CS361",  "Fall", 2022)

    def test_Semester(self):
        with self.assertRaises(ValueError, msg="Semester must be Spring, Summer, Fall, or Winter"):
            Course.createCourse("CS361", "Spaghetti", 2022)

    def test_Year(self):
        with self.assertRaises(TypeError, msg="Year must be an integer"):
            Course.createCourse("CS361", "Fall", "Jinkies")


class TestEditCourse(unittest.TestCase):

    def setUp(self):
        Scheduler.models.Course(number="CS361", semester="Fall", year=2022)

    def test_SuccessfulEdit(self):
        Course.editCourse("CS361", "CS458", "Spring", 2023)
        course458 = Course.objects.get(number="CS458")
        self.assertEqual(course458.number, "CS458", msg="Course Number not updated correctly")
        self.assertEqual(course458.semester, "Spring", msg="Semester not updated correctly")
        self.assertEqual(course458.year, 2023, msg="Year not updated correctly")

    def test_NullEdit(self):
        Course.editCourse("CS361", None, None, None)
        with self.assertRaises(NameError, msg="Course not found, Number shouldn't have updated"):
            course361 = Course.objects.get(number="CS361")
        self.assertEqual(course361.semester, "Fall", msg="Semester should not have updated to None")
        self.assertEqual(course361.year, 2022, msg="Year should not have updated to None")

    def test_PartialEdit(self):
        Course.editCourse("CS361", None, "Fall", None)
        with self.assertRaises(NameError, msg="Course not found, Number shouldn't have updated"):
            course361 = Course.objects.get(number="CS361")
        self.assertEqual(course361.semester, "Fall", msg="Semester should have updated to Fall")
        self.assertEqual(course361.year, 2022, msg="Year should not have updated to None")

    def test_NoSearchName(self):
        with self.assertRaises(TypeError, msg="Must provide a valid course"):
            Course.editCourse(None, "CS458", "Fall", 2022)

    def test_WrongSearchName(self):
        with self.assertRaises(TypeError, msg="Must provide a valid course"):
            Course.editCourse("CS999", "CS458", "Fall", 2022)

    def test_InvalidArg(self):
        with self.assertRaises(TypeError, msg="wrong Arg Type"):
            Course.editCourse("CS361", Course, "Fall", 2022)

    def test_InvalidArg2(self):
        with self.assertRaises(TypeError, msg="wrong Arg Type"):
            Course.editCourse("CS361", "CS458", Course, 2022)

    def test_InvalidArg3(self):
        with self.assertRaises(TypeError, msg="wrong Arg Type"):
            Course.editCourse("CS361", "CS458", "Fall", "Dino Nuggets")

    def test_NoArg(self):
        with self.assertRaises(TypeError, msg="not enough Arg"):
            Course.editCourse()

    def test_OneArg(self):
        with self.assertRaises(TypeError, msg="not enough Arg"):
            Course.editCourse("CS361")

    def test_TwoArg(self):
        with self.assertRaises(TypeError, msg="not enough Arg"):
            Course.editCourse("CS361", 2022)

    def test_ThreeArg(self):
        with self.assertRaises(TypeError, msg="not enough Arg"):
            Course.editCourse("CS361", "CS458", 2022)

    def test_FiveArg(self):
        with self.assertRaises(TypeError, msg="not enough Arg"):
            Course.editCourse("CS361", "C458", "Fall", 2022, "Banana Pickles")

    def test_InvalidName(self):
        with self.assertRaises(KeyError, msg="Key(Course) already exists"):
            Course.editCourse("CS361", "Fall", 2022)




