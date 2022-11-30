import Scheduler.models
from classes.course import Course
import unittest
from Scheduler.models import Course


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

    def test_OneArg(self):
        with self.assertRaises(TypeError, msg="not enough Arg"):
            Course.createCourse("CS361")

    def test_TwoArg(self):
        with self.assertRaises(TypeError, msg="not enough Arg"):
            Course.createCourse("CS361", "2022")

    def test_InvalidName(self):
        Course.createCourse("CS361", "Fall", "2022")
        with self.assertRaises():
            for i in Scheduler.models.Course:
                pass




class TestEditCourse(unittest.TestCase):

    def test_SuccessfulEdit(self):
        pass

