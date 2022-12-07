import Scheduler.models
from classes.course import Course
import unittest


class TestCreate(unittest.TestCase):
    def test_CreateWithSet(self):
        Course361 = Course()
        Course361.setNumber("CS361")
        Course361.setName("Intro")
        Course361.setDescription("Description")
        Course361.setInstructor("Mr Bean")
        Course361.setSemester("Fall")
        Course361.setYear(2022)
        Course361.save()
        self.assertEqual(self.models.Course.objects.getNumber(), "CS361", msg="Course Number Not Correct")
        self.assertEqual(self.models.Course.objects.getName(), "Intro", msg="Course Name Not Correct")
        self.assertEqual(self.models.Course.objects.getDescription(), "Description", msg="Course Description Not "
                                                                                         "Correct")
        self.assertEqual(self.models.Course.objects.getInstructor(), "Mr Bean", msg="Course Instructor Not Correct")
        self.assertEqual(self.models.Course.objects.getSemester(), "Fall", msg="Course Semester Not Correct")
        self.assertEqual(self.models.Course.objects.getYear(), 2022, msg="Course Year Not Correct")

    def test_CreateWithInit(self):
        Course361 = Course("CS361", "Intro", "Description", "Mr Bean", "Fall", 2022)
        self.assertEqual(Course361.getNumber(), "CS361", msg="Course Number Not Correct")
        self.assertEqual(Course361.getName(), "Intro", msg="Course Name Not Correct")
        self.assertEqual(Course361.getDescription(), "Description", msg="Course Description Not Correct")
        self.assertEqual(Course361.getInstructor(), "Mr Bean", msg="Course Instructor Not Correct")
        self.assertEqual(Course361.getSemester(), "Fall", msg="Course Semester Not Correct")
        self.assertEqual(Course361.getYear(), 2022, msg="Course Year Not Correct")

    def test_OneArgument(self):
        with self.assertRaises(TypeError, msg="Not Enough Arguments"):
            Course01 = Course("CS361")

    def test_TwoArguments(self):
        with self.assertRaises(TypeError, msg="Not Enough Arguments"):
            Course01 = Course("CS361", "Intro")

    def test_ThreeArguments(self):
        with self.assertRaises(TypeError, msg="Not Enough Arguments"):
            Course01 = Course("CS361", "Intro", "Description")

    def test_FourArguments(self):
        with self.assertRaises(TypeError, msg="Not Enough Arguments"):
            Course01 = Course("CS361", "Intro", "Description", "Mr Bean")

    def test_FiveArguments(self):
        with self.assertRaises(TypeError, msg="Not Enough Arguments"):
            Course01 = Course("CS361", "Intro", "Description", "Mr Bean", "Fall")

    def test_MoreArguments(self):
        with self.assertRaises(TypeError, msg="Too Many Arguments"):
            Course01 = Course("CS361", "Intro", "Description", "Mr Bean", "Fall", 2022, "Oops")

    def test_InvalidNumber(self):
        Course01 = Course()
        with self.assertRaises(TypeError, msg="Invalid Number Argument"):
            Course01.setNumber(361)

    def test_InvalidNameType(self):
        Course01 = Course()
        with self.assertRaises(TypeError, msg="Invalid Name Argument"):
            Course01.setName(999)

    def test_InvalidNameValue(self):
        Course01 = Course()
        with self.assertRaises(ValueError, msg="Invalid Name Argument"):
            Course01.setName("CS250.5")

    def test_InvalidDescription(self):
        Course01 = Course()
        with self.assertRaises(TypeError, msg="Invalid Description Argument"):
            Course01.setDescription(1234)

    def test_InvalidInstructor(self):
        Course01 = Course()
        with self.assertRaises(TypeError, msg="Invalid Instructor Argument"):
            Course01.setInstructor(9876)

    def test_InvalidSemesterType(self):
        Course01 = Course()
        with self.assertRaises(TypeError, msg="Invalid Semester Argument"):
            Course01.setSemester(123)

    def test_InvalidSemesterValue(self):
        Course01 = Course()
        with self.assertRaises(ValueError, msg="Invalid Semester Argument"):
            Course01.setSemester("Spaghetti")

    def test_InvalidYear(self):
        Course01 = Course()
        with self.assertRaises(TypeError, msg="Invalid Year Argument"):
            Course01.setYear("2022")

    def test_DuplicateName(self):
        Course01 = Course()
        Course01.setNumber("CS361")
        Course01.setName("Intro")
        Course01.setDescription("Description")
        Course01.setInstructor("Mr Bean")
        Course01.setSemester("Fall")
        Course01.setYear(2022)
        Course01.save()
        Course02 = Course()
        with self.assertRaises(KeyError, msg="Course Already Exists"):
            Course02.setNumber("CS361")
