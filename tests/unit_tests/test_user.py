from django.contrib.auth import get_user_model
from django.test import TestCase
from Scheduler.models import AppUser
from Scheduler.models import UserCourse
from Scheduler.models import Course
from Scheduler.models import Section
from Scheduler.classes import app_user


class TestInit(TestCase):
    def test_no_arg(self):
        with self.assertRaises(TypeError, msg="Must have at least panther ID"):
            a = app_user()

    def test_required_arg(self):
        a = app_user(12345, "test@test.com", "goodpassword")
        self.assertTrue(AppUser.objects.filter(pID=12345).exists())

    def test_all_arg(self):
        a = app_user(pID=123456789,
                    email='user@user.com',
                    password='foo',
                    first_name='John',
                    last_name='Doe',
                    phone_number='1234567890',
                    address='123 Main St',
                    city='New York',
                    state='NY',
                    zip_code='12345')
        self.assertTrue(AppUser.objects.filter(pID=123456789).exists())
    def test_invalid_arg(self):
        with self.assertRaises(TypeError, msg="Invalid type"):
            a = app_user("invalid ID")

    def test_repeated_id(self):
        a = app_user(123)
        with self.assertRaises(TypeError, msg="ID is not unique"):
            b = app_user(123)

class TestGetPID(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                            email='user@user.com',
                            password='foo',
                            first_name='John',
                            last_name='Doe',
                            phone_number='1234567890',
                            address='123 Main St',
                            city='New York',
                            state='NY',
                            zip_code='12345')
    def test_successful_call(self):
        self.assertEqual(self.user.getPID, 123456789)

class TestGetEmail(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                            email='user@user.com',
                            password='foo',
                            first_name='John',
                            last_name='Doe',
                            phone_number='1234567890',
                            address='123 Main St',
                            city='New York',
                            state='NY',
                            zip_code='12345')
    def test_successful_call(self):
        self.assertEqual(self.user.getEmail, 'user@user.com')

class TestSetEmail(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                            email='user@user.com',
                            password='foo',
                            first_name='John',
                            last_name='Doe',
                            phone_number='1234567890',
                            address='123 Main St',
                            city='New York',
                            state='NY',
                            zip_code='12345')

    def test_successful_set(self):
        self.user.setEmail('new@new.com')
        self.assertEqual(AppUser.objects.get(pID=123456789).email, 'new@new.com')

class TestGetFirstName(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                            email='user@user.com',
                            password='foo',
                            first_name='John',
                            last_name='Doe',
                            phone_number='1234567890',
                            address='123 Main St',
                            city='New York',
                            state='NY',
                            zip_code='12345')
    def test_successful_call(self):
        self.assertEqual(self.user.getFirstName, 'John')

class TestSetFirstName(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                            email='user@user.com',
                            password='foo',
                            first_name='John',
                            last_name='Doe',
                            phone_number='1234567890',
                            address='123 Main St',
                            city='New York',
                            state='NY',
                            zip_code='12345')

    def test_successful_set(self):
        self.user.setFirstName('Michael')
        self.assertEqual(AppUser.objects.get(pID=123456789).first_name, 'Michael')

class TestGetLastName(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                            email='user@user.com',
                            password='foo',
                            first_name='John',
                            last_name='Doe',
                            phone_number='1234567890',
                            address='123 Main St',
                            city='New York',
                            state='NY',
                            zip_code='12345')
    def test_successful_call(self):
        self.assertEqual(self.user.getLastName, 'Doe')

class TestSetLastName(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                            email='user@user.com',
                            password='foo',
                            first_name='John',
                            last_name='Doe',
                            phone_number='1234567890',
                            address='123 Main St',
                            city='New York',
                            state='NY',
                            zip_code='12345')

    def test_successful_set(self):
        self.user.setLastName('Smith')
        self.assertEqual(AppUser.objects.get(pID=123456789).last_name, 'Smith')
class TestGetName(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                            email='user@user.com',
                            password='foo',
                            first_name='John',
                            last_name='Doe',
                            phone_number='1234567890',
                            address='123 Main St',
                            city='New York',
                            state='NY',
                            zip_code='12345')
    def test_successful_call(self):
        self.assertEqual(self.user.getName, 'John Doe')

class TestSetName(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                            email='user@user.com',
                            password='foo',
                            first_name='John',
                            last_name='Doe',
                            phone_number='1234567890',
                            address='123 Main St',
                            city='New York',
                            state='NY',
                            zip_code='12345')

    def test_successful_set(self):
        self.user.setName('Michael Smith')
        self.assertEqual(AppUser.objects.get(pID=123456789).first_name, 'Michael')
        self.assertEqual(AppUser.objects.get(pID=123456789).last_name, 'Smith')

class TestGetPhone(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                            email='user@user.com',
                            password='foo',
                            first_name='John',
                            last_name='Doe',
                            phone_number='1234567890',
                            address='123 Main St',
                            city='New York',
                            state='NY',
                            zip_code='12345')
    def test_successful_call(self):
        self.assertEqual(self.user.getPhone, '1234567890')


class TestSetPhone(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                             email='user@user.com',
                             password='foo',
                             first_name='John',
                             last_name='Doe',
                             phone_number='1234567890',
                             address='123 Main St',
                             city='New York',
                             state='NY',
                             zip_code='12345')

    def test_successful_set(self):
        self.user.setPhone('4140001111')
        self.assertEqual(AppUser.objects.get(pID=123456789).phone_number, '4140001111')

    def test_invalid_number(self):
        with self.assertRaises(TypeError, msg="Invalid phone number"):
            self.user.setPhone("abcdefg")

class TestGetAddress(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                            email='user@user.com',
                            password='foo',
                            first_name='John',
                            last_name='Doe',
                            phone_number='1234567890',
                            address='123 Main St',
                            city='New York',
                            state='NY',
                            zip_code='12345')
    def test_successful_call(self):
        self.assertEqual(self.user.getAddress, '123 Main St')

class TestSetAddress(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                             email='user@user.com',
                             password='foo',
                             first_name='John',
                             last_name='Doe',
                             phone_number='1234567890',
                             address='123 Main St',
                             city='New York',
                             state='NY',
                             zip_code='12345')

    def test_successful_set(self):
        self.user.setAddress('456 New Rd')
        self.assertEqual(AppUser.objects.get(pID=123456789).address, '456 New Rd')

class TestGetCity(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                            email='user@user.com',
                            password='foo',
                            first_name='John',
                            last_name='Doe',
                            phone_number='1234567890',
                            address='123 Main St',
                            city='New York',
                            state='NY',
                            zip_code='12345')
    def test_successful_call(self):
        self.assertEqual(self.user.getCity, 'New York')

class TestSetCity(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                             email='user@user.com',
                             password='foo',
                             first_name='John',
                             last_name='Doe',
                             phone_number='1234567890',
                             address='123 Main St',
                             city='New York',
                             state='NY',
                             zip_code='12345')

    def test_successful_set(self):
        self.user.setCity('Milwaukee')
        self.assertEqual(AppUser.objects.get(pID=123456789).city, 'Milwaukee')

    def test_invalid_arg(self):
        with self.assertRaises(TypeError, msg="Invalid city"):
            self.user.setCity(123)
class TestGetState(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                             email='user@user.com',
                             password='foo',
                             first_name='John',
                             last_name='Doe',
                             phone_number='1234567890',
                             address='123 Main St',
                             city='New York',
                             state='NY',
                             zip_code='12345')

    def test_successful_call(self):
        self.assertEqual(self.user.getState, 'NY')

class TestSetState(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                             email='user@user.com',
                             password='foo',
                             first_name='John',
                             last_name='Doe',
                             phone_number='1234567890',
                             address='123 Main St',
                             city='New York',
                             state='NY',
                             zip_code='12345')

    def test_successful_set(self):
        self.user.setState('WI')
        self.assertEqual(AppUser.objects.get(pID=123456789).state, 'WI')

    def test_invalid_arg(self):
        with self.assertRaises(TypeError, msg="Invalid state"):
            self.user.setState(123)
class TestGetZip(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                            email='user@user.com',
                            password='foo',
                            first_name='John',
                            last_name='Doe',
                            phone_number='1234567890',
                            address='123 Main St',
                            city='New York',
                            state='NY',
                            zip_code='12345')
    def test_successful_call(self):
        self.assertEqual(self.user.getZip, '12345')

class TestSetZip(TestCase):
    def setUp(self):
        self.user = app_user(pID=123456789,
                             email='user@user.com',
                             password='foo',
                             first_name='John',
                             last_name='Doe',
                             phone_number='1234567890',
                             address='123 Main St',
                             city='New York',
                             state='NY',
                             zip_code='12345')

    def test_successful_set(self):
        self.user.setZip('54321')
        self.assertEqual(AppUser.objects.get(pID=123456789).zip_code, '54321')


class TestGetCourses(TestCase):
    def setUp(self):
        #create a couple users
        self.user = app_user(123, "user@test.com", "pass")
        self.user2 = app_user(456, "user2@test.com", "pass")

        #create a couple courses
        a = Course(courseID="CS 361 XX", name="Intro to SE", semester="F", year=2022)
        a.save()

        b = Course(courseID="CS 337 XX", name="System Programming", semester="F", year=2022)
        b.save()

        c = Course(courseID="CS 361 X", name="Intro to SE", semester="F", year=2022)
        c.save()

        #create some connections between them
        a = UserCourse(user=123, course="CS 361 XX")
        a.save()

        b = UserCourse(user=123, course="CS 337 XX")
        b.save()
    def test_successful_call(self):

        list = self.user.getCourses()
        self.assertEqual(list[0], "CS 361 XX")
        self.assertEqual(list[1], "CS 337 XX")

class TestAddCourse(TestCase):
    def setUp(self):
        # create a couple users
        self.user = app_user(123, "user@test.com", "pass")
        self.user2 = app_user(456, "user2@test.com", "pass")

        # create a couple courses
        a = Course(courseID="CS 361 XX", name="Intro to SE", semester="F", year=2022)
        a.save()

        b = Course(courseID="CS 337 XX", name="System Programming", semester="F", year=2022)
        b.save()

        c = Course(courseID="CS 361 X", name="Intro to SE", semester="F", year=2022)
        c.save()

        # create some connections between them
        a = UserCourse(user=123, course="CS 361 XX")
        a.save()

        b = UserCourse(user=123, course="CS 337 XX")
        b.save()

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
        self.user = app_user(123, "user@test.com", "pass")
        self.user2 = app_user(456, "user2@test.com", "pass")

        # create a couple courses
        a = Course(courseID="CS 361 XX", name="Intro to SE", semester="F", year=2022)
        a.save()

        b = Course(courseID="CS 337 XX", name="System Programming", semester="F", year=2022)
        b.save()

        c = Course(courseID="CS 361 X", name="Intro to SE", semester="F", year=2022)
        c.save()

        # create some connections between them
        a = UserCourse(user=123, course="CS 361 XX")
        a.save()

        b = UserCourse(user=123, course="CS 337 XX")
        b.save()

    def test_successful_remove(self):
        self.user.removeCourse("CS 361 XX")
        list = self.user.getCourses()
        self.assertEqual(list.len(), 1)
        self.assertEqual(list[0], "CS 337 XX")

    def test_invalid_course(self):
        with self.assertRaises(TypeError, msg="Invalid section"):
            self.user.removeCourse("Something")


class TestGetSections(TestCase):
    def setUp(self):
        #create a couple users
        self.user = app_user(123, "user@test.com", "pass")
        self.use2 = app_user(456, "user2@test.com", "pass")

        #create a couple courses
        a = Course(courseID="CS 361 XX", name="Intro to SE", semester="F", year=2022)
        a.save()

        b = Course(courseID="CS 337 XX", name="System Programming", semester="F", year=2022)
        b.save()

        c = Course(courseID="CS 361 X", name="Intro to SE", semester="F", year=2022)
        c.save()

        #create a couple sections
        d = Section(sectionID="CS 361 802", courseID="CS 361 XX", user=123)
        e = Section(sectionID="CS 337 801", courseID="CS 337 XX", user=123)
        f = Section(sectionID="CS 361 803", courseID="CS 361 XX", user=456)

    def test_successful_call(self):
        #assumes getSections works
        list = self.user.getSections()
        self.assertEqual(list[0], "CS 361 802")
        self.assertEqual(list[1], "CS 337 801")

class TestAddSection(TestCase):
    def setUp(self):
        #create a couple users
        self.user = app_user(123, "user@test.com", "pass")
        self.use2 = app_user(456, "user2@test.com", "pass")

        #create a couple courses
        a = Course(courseID="CS 361 XX", name="Intro to SE", semester="F", year=2022)
        a.save()

        b = Course(courseID="CS 337 XX", name="System Programming", semester="F", year=2022)
        b.save()

        c = Course(courseID="CS 361 X", name="Intro to SE", semester="F", year=2022)
        c.save()

        #create a couple sections
        d = Section(sectionID="CS 361 802", courseID="CS 361 XX", user=123)
        e = Section(sectionID="CS 337 801", courseID="CS 337 XX", user=123)
        f = Section(sectionID="CS 361 803", courseID="CS 361 XX", user=456)
        g = Section(sectionID="CS 337 802", courseID="CS 337 XX", user=None)

    def test_successful_add(self):
        self.user.addSection("CS 337 802")
        #assumes getSections() works
        list = self.user.getSections()
        self.assertEqual(list.len(), 3)
        self.assertEqual(list[0], "CS 361 802")
        self.assertEqual(list[1], "CS 337 801")
        self.assertEqual(list[2], "CS 337 802")

    def test_invalid_section(self):
        with self.assertRaises(TypeError, msg="Invalid section"):
            self.user.addSection("Something")


class TestRemoveSection(TestCase):
    def setUp(self):
        # create a couple users
        self.user = app_user(123, "user@test.com", "pass")
        self.use2 = app_user(456, "user2@test.com", "pass")

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
        self.assertEqual(list.len(), 1)
        self.assertEqual(list[0], "CS 337 801")


    def test_invalid_section(self):
        with self.assertRaises(TypeError, msg="Invalid section"):
            self.user.removeSection("Something")






# class UsersManagersTests(TestCase):
#     def test_create_user(self):
#         user_model = get_user_model()
#         user = user_model.objects.create_user(email='normal@user.com', password='foo')
#         self.assertEqual(user.email, 'normal@user.com')
#         self.assertTrue(user.is_active)
#         self.assertFalse(user.is_staff)
#         self.assertFalse(user.is_superuser)
#         try:
#             # username is None for the AbstractUser option
#             # username does not exist for the AbstractBaseUser option
#             self.assertIsNone(user.username)
#         except AttributeError:
#             pass
#         with self.assertRaises(TypeError):
#             user_model.objects.create_user()
#         with self.assertRaises(TypeError):
#             user_model.objects.create_user(email='')
#         with self.assertRaises(ValueError):
#             user_model.objects.create_user(email='', password="foo")
#
#     def test_create_superuser(self):
#         user_model = get_user_model()
#         admin_user = user_model.objects.create_superuser(email='super@user.com', password='foo')
#         self.assertEqual(admin_user.email, 'super@user.com')
#         self.assertTrue(admin_user.is_active)
#         self.assertTrue(admin_user.is_staff)
#         self.assertTrue(admin_user.is_superuser)
#         try:
#             # username is None for the AbstractUser option
#             # username does not exist for the AbstractBaseUser option
#             self.assertIsNone(admin_user.username)
#         except AttributeError:
#             pass
#         with self.assertRaises(ValueError):
#             user_model.objects.create_superuser(
#                 email='super@user.com', password='foo', is_superuser=False)
#
#
# class UserCreationTests(TestCase):
#     def test_user_creation_success(self):
#         user_model = get_user_model()
#         user = user_model.objects.create_user(pID=123456789, email='user@user.com', password='foo')
#         self.assertEqual(user.pID, 123456789)
#         self.assertEqual(user.email, 'user@user.com')
#         self.assertTrue(user.is_active)
#         self.assertFalse(user.is_staff)
#         self.assertFalse(user.is_superuser)
#
#     def test_user_creation_failure_invalid_email(self):
#         user_model = get_user_model()
#         with self.assertRaises(ValueError, msg='Email must be valid'):
#             user_model.objects.create_user(pID=123456789, email='user', password='foo')
#         with self.assertRaises(ValueError, msg='Email must be set'):
#             user_model.objects.create_user(pID=123456789, email='', password='foo')
#         with self.assertRaises(ValueError, msg='Email must be set'):
#             user_model.objects.create_user(pID=123456789, email=None, password='foo')
#
#     def test_user_creation_failure_invalid_pID(self):
#         user_model = get_user_model()
#         with self.assertRaises(ValueError, msg='pID must be valid'):
#             user_model.objects.create_user(pID=12345678, email='user@user.com', password='foo')
#         with self.assertRaises(ValueError, msg='pID must be valid'):
#             user_model.objects.create_user(pID='12345678', email='user@user.com', password='foo')
#         with self.assertRaises(ValueError, msg='pID must be set'):
#             user_model.objects.create_user(pID=None, email='user@user.com', password='foo')
#
#     def test_user_creation_failure_invalid_password(self):
#         user_model = get_user_model()
#         with self.assertRaises(ValueError, msg='Password must be set'):
#             user_model.objects.create_user(pID=123456789, email='user@user.com', password='')
#
#
# class LoginTests(TestCase):
#     def setUp(self) -> None:
#         user_model = get_user_model()
#         user_model.objects.create_user(pID=123456789, email='user@user.com', password='foo')
#
#     def test_login_success(self):
#         self.assertTrue(self.client.login(email='user@user.com', password='foo'),
#                         msg='Login with valid email and password should succeed')
#
#     def test_login_failure_invalid_email(self):
#         self.assertFalse(self.client.login(email='user', password='foo'),
#                          msg='Login with invalid email should fail')
#         self.assertFalse(self.client.login(email='', password='foo'),
#                          msg='Login with blank email should fail')
#         self.assertFalse(self.client.login(email=None, password='foo'),
#                          msg='Login with None email should fail')
#
#     def test_login_failure_invalid_password(self):
#         self.assertFalse(self.client.login(email='user@user.com', password=''),
#                          msg='Login with blank password should fail')
#         self.assertFalse(self.client.login(email='user@user.com', password='bar'),
#                          msg='Login with invalid password should fail')
#
#
# class UserDeletionTests(TestCase):
#     def setUp(self) -> None:
#         user_model = get_user_model()
#         user_model.objects.create_user(pID=123456789, email='user@user.com', password='foo')
#
#     def test_user_deletion_success(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(email='user@user.com')
#         user.delete()
#         self.assertEqual(user_model.objects.count(), 0, msg='User should be deleted')
#
#     def test_user_deletion_failure_does_not_exist(self):
#         user_model = get_user_model()
#         with self.assertRaises(user_model.DoesNotExist, msg='User does not exist'):
#             user_model.objects.get(email='dne@user.com').delete()
#
#
# class UserUpdateTests(TestCase):
#     def setUp(self) -> None:
#         user_model = get_user_model()
#         user_model.objects.create_user(
#             pID=123456789,
#             email='user@user.com',
#             password='foo',
#             first_name='John',
#             last_name='Doe',
#             phone_number='1234567890',
#             address='123 Main St',
#             city='New York',
#             state='NY',
#             zip_code='12345'
#         )
#
#     def test_user_update_success_email(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         user.email = 'new@user.com'
#         user.save()
#         self.assertEqual(user_model.objects.get(pID=123456789).email, 'new@user.com',
#                          msg='User email should be updated')
#
#     def test_user_update_success_password(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         user.set_password('bar')
#         user.save()
#         self.assertTrue(self.client.login(pID=123456789, password='bar'),
#                         msg='Login with new password should succeed')
#
#     def test_user_update_success_first_name(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         user.first_name = 'Jane'
#         user.save()
#         self.assertEqual(user_model.objects.get(pID=123456789).first_name, 'Jane',
#                          msg='User first name should be updated')
#
#     def test_user_update_success_last_name(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         user.last_name = 'Smith'
#         user.save()
#         self.assertEqual(user_model.objects.get(pID=123456789).last_name, 'Smith',
#                          msg='User last name should be updated')
#
#     def test_user_update_success_phone_number(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         user.phone_number = '0987654321'
#         user.save()
#         self.assertEqual(user_model.objects.get(pID=123456789).phone_number, '0987654321',
#                          msg='User phone number should be updated')
#
#     def test_user_update_success_address(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         user.address = '456 Main St'
#         user.save()
#         self.assertEqual(user_model.objects.get(pID=123456789).address, '456 Main St',
#                          msg='User address should be updated')
#
#     def test_user_update_success_city(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         user.city = 'Los Angeles'
#         user.save()
#         self.assertEqual(user_model.objects.get(pID=123456789).city, 'Los Angeles',
#                          msg='User city should be updated')
#
#     def test_user_update_success_state(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         user.state = 'CA'
#         user.save()
#         self.assertEqual(user_model.objects.get(pID=123456789).state, 'CA',
#                          msg='User state should be updated')
#
#     def test_user_update_success_zip_code(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         user.zip_code = '54321'
#         user.save()
#         self.assertEqual(user_model.objects.get(pID=123456789).zip_code, '54321',
#                          msg='User zip code should be updated')
#
#     def test_user_update_failure_email(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         with self.assertRaises(ValueError, msg='Email must be valid'):
#             user.email = 'user'
#             user.save()
#         with self.assertRaises(ValueError, msg='Email must be set'):
#             user.email = ''
#             user.save()
#         with self.assertRaises(ValueError, msg='Email must be set'):
#             user.email = None
#             user.save()
#
#     def test_user_update_failure_password(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         with self.assertRaises(ValueError, msg='Password must be set'):
#             user.set_password('')
#             user.save()
#         with self.assertRaises(ValueError, msg='Password must be set'):
#             user.set_password(None)
#             user.save()
#
#     def test_user_update_failure_first_name(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         with self.assertRaises(ValueError, msg='First name must be set'):
#             user.first_name = ''
#             user.save()
#         with self.assertRaises(ValueError, msg='First name must be set'):
#             user.first_name = None
#             user.save()
#
#     def test_user_update_failure_last_name(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         with self.assertRaises(ValueError, msg='Last name must be set'):
#             user.last_name = ''
#             user.save()
#         with self.assertRaises(ValueError, msg='Last name must be set'):
#             user.last_name = None
#             user.save()
#
#     def test_user_update_failure_phone_number(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         with self.assertRaises(ValueError, msg='Phone number must be set'):
#             user.phone_number = ''
#             user.save()
#         with self.assertRaises(ValueError, msg='Phone number must be set'):
#             user.phone_number = None
#             user.save()
#
#     def test_user_update_failure_address(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         with self.assertRaises(ValueError, msg='Address must be set'):
#             user.address = ''
#             user.save()
#         with self.assertRaises(ValueError, msg='Address must be set'):
#             user.address = None
#             user.save()
#
#     def test_user_update_failure_city(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         with self.assertRaises(ValueError, msg='City must be set'):
#             user.city = ''
#             user.save()
#         with self.assertRaises(ValueError, msg='City must be set'):
#             user.city = None
#             user.save()
#
#     def test_user_update_failure_state(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         with self.assertRaises(ValueError, msg='State must be set'):
#             user.state = ''
#             user.save()
#         with self.assertRaises(ValueError, msg='State must be set'):
#             user.state = None
#             user.save()
#
#     def test_user_update_failure_zip_code(self):
#         user_model = get_user_model()
#         user = user_model.objects.get(pID=123456789)
#         with self.assertRaises(ValueError, msg='Zip code must be set'):
#             user.zip_code = ''
#             user.save()
#         with self.assertRaises(ValueError, msg='Zip code must be set'):
#             user.zip_code = None
#             user.save()
