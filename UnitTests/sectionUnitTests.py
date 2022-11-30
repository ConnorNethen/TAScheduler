from classes.section import Section
import unittest


class TestCreate(unittest.TestCase):

    def test_SuccessfulCreate(self):
        Section.createSection("001", "CS361", "Lab", "Tuesday 2:30")
        section361lab = Section.objects.get(number="CS361")
        self.assertEqual(section361lab.number, "001", msg="Section Number not correct")
        self.assertEqual(section361lab.course, "CS361", msg="Course Name not correct")
        self.assertEqual(section361lab.type, "Lab", msg="Type of Section not correct")
        self.assertEqual(section361lab.time, "Tuesday 2:30", msg="Time not correct")

    def test_InvalidArg(self):
        with self.assertRaises(TypeError, msg="wrong Arg Type"):
            Section.createSection(Section, "CS361", "Lab", "Tuesday 2:30")

    def test_OneArg(self):
        with self.assertRaises(TypeError, msg="not enough Arg"):
            Section.createSection("CS361")

    def test_TwoArg(self):
        with self.assertRaises(TypeError, msg="not enough Arg"):
            Section.createSection("001", "CS361")

    def test_ThreeArg(self):
        with self.assertRaises(TypeError, msg="not enough Arg"):
            Section.createSection("001", "CS361", "Lab")

    def test_InvalidName(self):
        Section.createSection("001", "CS361", "Lab", "Tuesday 2:30")
        with self.assertRaises(KeyError, msg="Key(Section Number) already exists"):
            Section.createSection("001", "CS361", "Lab", "Tuesday 2:30")
