from django.test import TestCase, Client
from Scheduler.models import Course, UserCourse, Section, AppUser


class CreateSection(TestCase):
    tester = None

    def setUp(self):
        Address("street1", "street2", "city", "state", "12345")
        User("1234", "username", "password", "first", "last",
             ContactInfo("email@abc.com", "123456789", "street1"),
             Status("A"))

    def test_sectionCreatedSuccessfully(self):
        tester = Client()
        response = tester.post('login/', {"username": "username", "password": "password"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        response = tester.post('index', {"Submit": "courses/new/"}, follow=True)
        self.assertRedircts(response, 'courses/new/', msg="Did not redirect to course create page")
        tester.post('courses/new/', {"courseNumber": "CS361", "semester": "Fall", "year": "2022",
                                     "sections": [["001", "CS361", "Lab", "Tuesday 2:30"]]}, follow=True)
        thisSection = Section.objects.get(number="001")
        self.assertIsNotNone(thisSection, msg="Section not created in database")
        self.assertEqual(thisSection.course, "CS361", msg="Course not correct in section")
        self.assertEqual(thisSection.type, "Lab", msg="Lab not correct for the section")

    def test_badInputSectionNumber(self):
        tester = Client()
        response = tester.post('login/', {"username": "username", "password": "password"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        response = tester.post('index', {"Submit": "courses/new/"}, follow=True)
        self.assertRedircts(response, 'courses/new/', msg="Did not redirect to course create page")
        response = tester.post('courses/new/', {"courseNumber": "CS361", "semester": "Fall", "year": "2022",
                                                "sections": [["one", "CS361", "notALab", "Tuesday 2:30"]]}, follow=True)
        self.assertEqual(response.context["message"], "section number has incorrect format, Try three numbers!",
                         msg="error message not populated for bad format of section number.")

    def test_badInputTime(self):
        tester = Client()
        response = tester.post('login/', {"username": "username", "password": "password"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        response = tester.post('index', {"Submit": "courses/new/"}, follow=True)
        self.assertRedircts(response, 'courses/new/', msg="Did not redirect to course create page")
        response = tester.post('courses/new/', {"courseNumber": "CS361", "semester": "4532134", "year": "2022",
                                                "sections": [["001", "CS361", "Lab", "notATime"]]}, follow=True)
        self.assertEqual(response.context["message"], "incorrect Time format, Try (day, hour:minute)",
                         msg="error message not populated for bad format of time.")

    def test_badInputTypeOfSection(self):
        tester = Client()
        response = tester.post('login/', {"username": "username", "password": "password"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        response = tester.post('index', {"Submit": "courses/new/"}, follow=True)
        self.assertRedircts(response, 'courses/new/', msg="Did not redirect to course create page")
        response = tester.post('courses/new/', {"courseNumber": "CS361", "semester": "Fall", "year": "2022",
                                                "sections": [["001", "CS361", "notALab", "Tuesday 2:30"]]}, follow=True)
        self.assertEqual(response.context["message"], "incorrect type of section, choose either Lab or Lecture",
                         msg="error message not populated for bad format of type of section.")

    def test_duplicate(self):
        tester = Client()
        Course("CS361", "Fall", "2022")
        response = tester.post('login/', {"username": "username", "password": "password"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        response = tester.post('index', {"Submit": "courses/new/"}, follow=True)
        self.assertRedircts(response, 'courses/new/', msg="Did not redirect to course create page")
        tester.post('courses/new/', {"courseNumber": "CS361", "semester": "Fall", "year": "2022",
                                     "sections": [["001", "CS361", "Lab", "Tuesday 2:30"][
                                                      "001", "CS361", "Lab", "Tuesday 2:30"]]}, follow=True)
        self.assertEqual(response.context["message"], "Section already exists", msg="error section existence.")

    def test_TACreate(self):
        tester = Client()
        User("123456TA", "usernameTA", "passwordTA", "firstTA", "lastTA",
             ContactInfo("emailTA@abc.com", "123456781", "street1"),
             Status("T"))
        response = tester.post('login/', {"username": "usernameTA", "password": "passwordTA"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        response = tester.post('index', {"Submit": "courses/new/"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to back to home page")
        self.assertEqual(response.context["message"], "Access Denied",
                         msg="error essay didnt populate for invalid status")

    def test_InstructorCreate(self):
        tester = Client()
        User("123456IN", "usernameIN", "passwordIN", "firstIN", "lastIN",
             ContactInfo("emailTA@abc.com", "123456781", "street1"),
             Status("I"))
        response = tester.post('login/', {"username": "usernameIN", "password": "passwordIN"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        response = tester.post('index', {"Submit": "courses/new/"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to back to home page")
        self.assertEqual(response.context["message"], "Access Denied",
                         msg="error essay didnt populate for invalid status")
