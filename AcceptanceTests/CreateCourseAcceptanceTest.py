from django.test import TestCase, Client
from Scheduler.classes.course import AppCourse
from Scheduler.models import Course, UserCourse, Section, AppUser


class CreateCourse(TestCase):
    tester = None

    def setUp(self):
        tester = Client()
        AppCourse("CS 361", "Intro", "F", 2022)

    def test_CourseCreatedSuccessfully(self):
        # tester = Client()
        response = self.tester.post('login/', {"username": "username", "password": "password"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        response = self.tester.post('index', {"Submit": "courses/new/"}, follow=True)
        self.assertRedircts(response, 'courses/new/', msg="Did not redirect to course create page")
        self.tester.post('courses/new/', {"courseID": "CS 361", "name": "Intro", "semester": "F", "year": 2022}, follow=True)
        thisCourse = Course.objects.get(name="CS 361")
        self.assertIsNotNone(thisCourse, msg="Course not created in database")
        self.assertEqual(thisCourse.name, "Intro", msg="name not correct in course")
        self.assertEqual(thisCourse.semester, "F", msg="Semester not correct in course")
        self.assertEqual(thisCourse.year, 2022, msg="year not correct for the course")

    def test_BadInputCourseNumber(self):
        #tester = Client()
        response = self.tester.post('login/', {"username": "username", "password": "password"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        response = self.tester.post('index', {"Submit": "courses/new/"}, follow=True)
        self.assertRedircts(response, 'courses/new/', msg="Did not redirect to course create page")
        response = self.tester.post('courses/new/', {"courseNumber": "1234", "semester": "Fall", "year": "2022"},
                               follow=True)
        self.assertEqual(response.context["message"],
                         "course number has incorrect format, Try 2 letters and three numbers!",
                         msg="error message not populated for bad format.")

    def test_BadInputSemester(self):
        #tester = Client()
        response = self.tester.post('login/', {"username": "username", "password": "password"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        response = self.tester.post('index', {"Submit": "courses/new/"}, follow=True)
        self.assertRedircts(response, 'courses/new/', msg="Did not redirect to course create page")
        response = self.tester.post('courses/new/', {"courseNumber": "CS361", "semester": "4532134", "year": "2022"},
                               follow=True)
        self.assertEqual(response.context["message"], "incorrect semester, Try spring, summer, fall or winter!",
                         msg="error message not populated for bad format.")

    def test_badInputYear(self):
        #tester = Client()
        response = self.tester.post('login/', {"username": "username", "password": "password"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        response = self.tester.post('index', {"Submit": "courses/new/"}, follow=True)
        self.assertRedircts(response, 'courses/new/', msg="Did not redirect to course create page")
        response = self.tester.post('courses/new/', {"courseNumber": "CS361", "semester": "Fall", "year": "abcde"},
                               follow=True)
        self.assertEqual(response.context["message"], "incorrect year, choose a year form 2015-2023",
                         msg="error message not populated for bad format.")

    def test_Duplicate(self):
        #tester = Client()
        #Course("CS361", "Fall", "2022")
        response = self.tester.post('login/', {"username": "username", "password": "password"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        response = self.tester.post('index', {"Submit": "courses/new/"}, follow=True)
        self.assertRedircts(response, 'courses/new/', msg="Did not redirect to course create page")
        response = self.tester.post('courses/new/', {"courseNumber": "CS361", "semester": "Fall", "year": "2022"},
                               follow=True)
        self.assertEqual(response.context["message"], "Course already exists", msg="error course existence.")

    # def test_TACreate(self):
    #     tester = Client()
    #     User("123456TA", "usernameTA", "passwordTA", "firstTA", "lastTA",
    #          ContactInfo("emailTA@abc.com", "123456781", "street1"),
    #          Status("T"))
    #     response = tester.post('login/', {"username": "usernameTA", "password": "passwordTA"}, follow=True)
    #     self.assertRedircts(response, 'index', msg="Did not redirect to home page")
    #     response = tester.post('index', {"Submit": "courses/new/"}, follow=True)
    #     self.assertRedircts(response, 'index', msg="Did not redirect to back to home page")
    #     self.assertEqual(response.context["message"], "Access Denied",
    #                      msg="error essay didnt populate for invalid status")
    #
    # def test_InstructorCreate(self):
    #     tester = Client()
    #     User("123456IN", "usernameIN", "passwordIN", "firstIN", "lastIN",
    #          ContactInfo("emailTA@abc.com", "123456781", "street1"),
    #          Status("I"))
    #     response = tester.post('login/', {"username": "usernameIN", "password": "passwordIN"}, follow=True)
    #     self.assertRedircts(response, 'index', msg="Did not redirect to home page")
    #     response = tester.post('index', {"Submit": "courses/new/"}, follow=True)
    #     self.assertRedircts(response, 'index', msg="Did not redirect to back to home page")
    #     self.assertEqual(response.context["message"], "Access Denied",
    #                      msg="error essay didnt populate for invalid status")
