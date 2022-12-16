from django.test import TestCase
from Scheduler.models import AppUser
from Scheduler.models import UserCourse
from Scheduler.models import Course
from Scheduler.models import Section
from Scheduler.classes.app_user import AppUserClass


class TestInit(TestCase):
    def test_no_arg(self):
        with self.assertRaises(TypeError, msg="Must have at least panther ID, email, pass"):
            a = AppUserClass()

    def test_required_arg(self):
        a = AppUserClass("12345", "test@test.com", "goodpassword")
        self.assertTrue(AppUser.objects.filter(pID="12345").exists())

    def test_all_arg(self):
        a = AppUserClass("123456789",
                         "user@user.com",
                         "foo",
                         'John',
                         'Doe',
                         '1234567890',
                         '123 Main St',
                         'New York',
                         'NY',
                         '12345')
        self.assertTrue(AppUser.objects.filter(pID="123456789").exists())

    def test_invalid_arg(self):
        with self.assertRaises(TypeError, msg="Invalid type"):
            a = AppUserClass("invalid ID")

    def test_repeated_id(self):
        a = AppUserClass("123", "string@email.com", "pass")
        with self.assertRaises(TypeError, msg="ID is not unique"):
            b = AppUserClass("123", "string2@email.com", "pass")


class TestGetPID(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_call(self):
        self.assertEqual(self.user.getPID, "123456789")


class TestGetEmail(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_call(self):
        self.assertEqual(self.user.getEmail, 'user@user.com')


class TestSetEmail(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_set(self):
        self.user.setEmail('new@new.com')
        self.assertEqual(AppUser.objects.get(pID="123456789").email, 'new@new.com')


class TestGetFirstName(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_call(self):
        self.assertEqual(self.user.getFirstName, 'John')


class TestSetFirstName(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_set(self):
        self.user.setFirstName('Michael')
        self.assertEqual(AppUser.objects.get(pID="123456789").first_name, 'Michael')


class TestGetLastName(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_call(self):
        self.assertEqual(self.user.getLastName, 'Doe')


class TestSetLastName(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_set(self):
        self.user.setLastName('Smith')
        self.assertEqual(AppUser.objects.get(pID="123456789").last_name, 'Smith')


class TestGetName(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_call(self):
        self.assertEqual(self.user.getFullName, 'John Doe')


class TestSetName(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_set(self):
        self.user.setFullName('Michael Smith')
        self.assertEqual(AppUser.objects.get(pID="123456789").first_name, 'Michael')
        self.assertEqual(AppUser.objects.get(pID="123456789").last_name, 'Smith')


class TestGetPhone(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_call(self):
        self.assertEqual(self.user.getPhone, '1234567890')


class TestSetPhone(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_set(self):
        self.user.setPhone('4140001111')
        self.assertEqual(AppUser.objects.get(pID="123456789").phone_number, '4140001111')

    def test_invalid_number(self):
        with self.assertRaises(TypeError, msg="Invalid phone number"):
            self.user.setPhone("abcdefg")


class TestGetAddress(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_call(self):
        self.assertEqual(self.user.getAddress, '123 Main St')


class TestSetAddress(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_set(self):
        self.user.setAddress('456 New Rd')
        self.assertEqual(AppUser.objects.get(pID="123456789").address, '456 New Rd')


class TestGetCity(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_call(self):
        self.assertEqual(self.user.getCity, 'New York')


class TestSetCity(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_set(self):
        self.user.setCity('Milwaukee')
        self.assertEqual(AppUser.objects.get(pID="123456789").city, 'Milwaukee')

    def test_invalid_arg(self):
        with self.assertRaises(TypeError, msg="Invalid city"):
            self.user.setCity(123)


class TestGetState(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_call(self):
        self.assertEqual(self.user.getState, 'NY')


class TestSetState(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_set(self):
        self.user.setState('WI')
        self.assertEqual(AppUser.objects.get(pID="123456789").state, 'WI')

    def test_invalid_arg(self):
        with self.assertRaises(TypeError, msg="Invalid state"):
            self.user.setState(123)


class TestGetZip(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_call(self):
        self.assertEqual(self.user.getZip, '12345')


class TestSetZip(TestCase):
    def setUp(self):
        self.user = AppUserClass("123456789",
                                 'user@user.com',
                                 'foo',
                                 'John',
                                 'Doe',
                                 "1234567890",
                                 "123 Main St",
                                 "New York",
                                 "NY",
                                 "12345")

    def test_successful_set(self):
        self.user.setZip('54321')
        self.assertEqual(AppUser.objects.get(pID="123456789").zip_code, '54321')


class TestGetCourses(TestCase):
    def setUp(self):
        # create a couple users
        self.user = AppUserClass("123", "user@test.com", "pass")
        self.user2 = AppUserClass("456", "user2@test.com", "pass")

        # create a couple courses
        a = Course(courseID="CS 361 XX", name="Intro to SE", semester="F", year=2022)
        a.save()

        b = Course(courseID="CS 337 XX", name="System Programming", semester="F", year=2022)
        b.save()

        c = Course(courseID="CS 361 X", name="Intro to SE", semester="F", year=2022)
        c.save()

        # create some connections between them
        d = UserCourse(user=self.user, course=a)
        d.save()

        e = UserCourse(user=self.user, course=b)
        e.save()

    def test_successful_call(self):
        list = self.user.getCourses()
        self.assertEqual(list[0], "CS 361 XX")
        self.assertEqual(list[1], "CS 337 XX")


class TestAddCourse(TestCase):
    def setUp(self):
        # create a couple users
        self.user = AppUserClass("123", "user@test.com", "pass")
        self.user2 = AppUserClass("456", "user2@test.com", "pass")

        # create a couple courses
        a = Course(courseID="CS 361 XX", name="Intro to SE", semester="F", year=2022)
        a.save()

        b = Course(courseID="CS 337 XX", name="System Programming", semester="F", year=2022)
        b.save()

        c = Course(courseID="CS 361 X", name="Intro to SE", semester="F", year=2022)
        c.save()

        # create some connections between them
        d = UserCourse(user=self.user, course=a)
        d.save()

        e = UserCourse(user=self.user, course=b)
        e.save()

    def test_successful_add(self):
        self.user.addCourse("CS 317 XX")
        list = self.user.getCourses()
        self.assertEqual(list[0], "CS 361 XX")
        self.assertEqual(list[1], "CS 337 XX")
        self.assertEqual(list[2], "CS 317 XX")

    def test_invalid_course(self):
        with self.assertRaises(TypeError, msg="Invalid section"):
            self.user.addCourse("Something")


class TestRemoveCourse(TestCase):
    def setUp(self):
        # create a couple users
        self.user = AppUserClass("123", "user@test.com", "pass")
        self.user2 = AppUserClass("456", "user2@test.com", "pass")

        # create a couple courses
        a = Course(courseID="CS 361 XX", name="Intro to SE", semester="F", year=2022)
        a.save()

        b = Course(courseID="CS 337 XX", name="System Programming", semester="F", year=2022)
        b.save()

        c = Course(courseID="CS 361 X", name="Intro to SE", semester="F", year=2022)
        c.save()

        # create some connections between them
        d = UserCourse(user=self.user, course=a)
        d.save()

        e = UserCourse(user=self.user, course=b)
        e.save()

    def test_successful_remove(self):
        self.user.removeCourse("CS 361 XX")
        list = self.user.getCourses()
        self.assertEqual(len(list), 1)
        self.assertEqual(list[0], "CS 337 XX")

    def test_invalid_course(self):
        with self.assertRaises(TypeError, msg="Invalid section"):
            self.user.removeCourse("Something")


class TestGetSections(TestCase):
    def setUp(self):
        # create a couple users
        self.user = AppUserClass("123", "user@test.com", "pass")
        self.user2 = AppUserClass("456", "user2@test.com", "pass")

        # create a couple courses
        a = Course(courseID="CS 361 XX", name="Intro to SE", semester="F", year=2022)
        a.save()

        b = Course(courseID="CS 337 XX", name="System Programming", semester="F", year=2022)
        b.save()

        c = Course(courseID="CS 361 X", name="Intro to SE", semester="F", year=2022)
        c.save()

        # create a couple sections
        d = Section(sectionID="CS 361 802", courseID=a, user=self.user)
        e = Section(sectionID="CS 337 801", courseID=b, user=self.user)
        f = Section(sectionID="CS 361 803", courseID=a, user=self.user2)

    def test_successful_call(self):
        # assumes getSections works
        list = self.user.getSections()
        self.assertEqual(list[0], "CS 361 802")
        self.assertEqual(list[1], "CS 337 801")


class TestAddSection(TestCase):
    def setUp(self):
        # create a couple users
        self.user = AppUserClass("123", "user@test.com", "pass")
        self.use2 = AppUserClass("456", "user2@test.com", "pass")

        # create a couple courses
        a = Course(courseID="CS 361 XX", name="Intro to SE", semester="F", year=2022)
        a.save()

        b = Course(courseID="CS 337 XX", name="System Programming", semester="F", year=2022)
        b.save()

        c = Course(courseID="CS 361 X", name="Intro to SE", semester="F", year=2022)
        c.save()

        # create a couple sections
        d = Section(sectionID="CS 361 802", courseID="CS 361 XX", user="123")
        e = Section(sectionID="CS 337 801", courseID="CS 337 XX", user="123")
        f = Section(sectionID="CS 361 803", courseID="CS 361 XX", user=456)
        g = Section(sectionID="CS 337 802", courseID="CS 337 XX", user=None)

    def test_successful_add(self):
        self.user.addSection("CS 337 802")
        # assumes getSections() works
        list = self.user.getSections()
        self.assertEqual(len(list), 3)
        self.assertEqual(list[0], "CS 361 802")
        self.assertEqual(list[1], "CS 337 801")
        self.assertEqual(list[2], "CS 337 802")

    def test_invalid_section(self):
        with self.assertRaises(TypeError, msg="Invalid section"):
            self.user.addSection("Something")


class TestRemoveSection(TestCase):
    def setUp(self):
        # create a couple users
        self.user = AppUserClass("123", "user@test.com", "pass")
        self.use2 = AppUserClass("456", "user2@test.com", "pass")

        # create a couple courses
        a = Course(courseID="CS 361 XX", name="Intro to SE", semester="F", year=2022)
        a.save()

        b = Course(courseID="CS 337 XX", name="System Programming", semester="F", year=2022)
        b.save()

        c = Course(courseID="CS 361 X", name="Intro to SE", semester="F", year=2022)
        c.save()

        # create a couple sections
        d = Section(sectionID="CS 361 802", courseID="CS 361 XX", user=123)
        e = Section(sectionID="CS 337 801", courseID="CS 337 XX", user=123)
        f = Section(sectionID="CS 361 803", courseID="CS 361 XX", user=456)

    def test_successful_remove(self):
        self.user.removeSection("CS 361 802")
        # assumes getSections() works
        list = self.user.getSections()
        self.assertEqual(len(list), 1)
        self.assertEqual(list[0], "CS 337 801")

    def test_invalid_section(self):
        with self.assertRaises(TypeError, msg="Invalid section"):
            self.user.removeSection("Something")

