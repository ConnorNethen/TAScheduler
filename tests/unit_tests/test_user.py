from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):
    def test_create_user(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            user_model.objects.create_user()
        with self.assertRaises(TypeError):
            user_model.objects.create_user(email='')
        with self.assertRaises(ValueError):
            user_model.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        user_model = get_user_model()
        admin_user = user_model.objects.create_superuser(email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            user_model.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)


class UserCreationTests(TestCase):
    def test_user_creation_success(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(pID=123456789, email='user@user.com', password='foo')
        self.assertEqual(user.pID, 123456789)
        self.assertEqual(user.email, 'user@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_user_creation_failure_invalid_email(self):
        user_model = get_user_model()
        with self.assertRaises(ValueError, msg='Email must be valid'):
            user_model.objects.create_user(pID=123456789, email='user', password='foo')
        with self.assertRaises(ValueError, msg='Email must be set'):
            user_model.objects.create_user(pID=123456789, email='', password='foo')
        with self.assertRaises(ValueError, msg='Email must be set'):
            user_model.objects.create_user(pID=123456789, email=None, password='foo')

    def test_user_creation_failure_invalid_pID(self):
        user_model = get_user_model()
        with self.assertRaises(ValueError, msg='pID must be valid'):
            user_model.objects.create_user(pID=12345678, email='user@user.com', password='foo')
        with self.assertRaises(ValueError, msg='pID must be valid'):
            user_model.objects.create_user(pID='12345678', email='user@user.com', password='foo')
        with self.assertRaises(ValueError, msg='pID must be set'):
            user_model.objects.create_user(pID=None, email='user@user.com', password='foo')

    def test_user_creation_failure_invalid_password(self):
        user_model = get_user_model()
        with self.assertRaises(ValueError, msg='Password must be set'):
            user_model.objects.create_user(pID=123456789, email='user@user.com', password='')


class LoginTests(TestCase):
    def setUp(self) -> None:
        user_model = get_user_model()
        user_model.objects.create_user(pID=123456789, email='user@user.com', password='foo')

    def test_login_success(self):
        self.assertTrue(self.client.login(email='user@user.com', password='foo'),
                        msg='Login with valid email and password should succeed')

    def test_login_failure_invalid_email(self):
        self.assertFalse(self.client.login(email='user', password='foo'),
                         msg='Login with invalid email should fail')
        self.assertFalse(self.client.login(email='', password='foo'),
                         msg='Login with blank email should fail')
        self.assertFalse(self.client.login(email=None, password='foo'),
                         msg='Login with None email should fail')

    def test_login_failure_invalid_password(self):
        self.assertFalse(self.client.login(email='user@user.com', password=''),
                         msg='Login with blank password should fail')
        self.assertFalse(self.client.login(email='user@user.com', password='bar'),
                         msg='Login with invalid password should fail')


class UserDeletionTests(TestCase):
    def setUp(self) -> None:
        user_model = get_user_model()
        user_model.objects.create_user(pID=123456789, email='user@user.com', password='foo')

    def test_user_deletion_success(self):
        user_model = get_user_model()
        user = user_model.objects.get(email='user@user.com')
        user.delete()
        self.assertEqual(user_model.objects.count(), 0, msg='User should be deleted')

    def test_user_deletion_failure_does_not_exist(self):
        user_model = get_user_model()
        with self.assertRaises(user_model.DoesNotExist, msg='User does not exist'):
            user_model.objects.get(email='dne@user.com').delete()


class UserUpdateTests(TestCase):
    def setUp(self) -> None:
        user_model = get_user_model()
        user_model.objects.create_user(
            pID=123456789,
            email='user@user.com',
            password='foo',
            first_name='John',
            last_name='Doe',
            phone_number='1234567890',
            address='123 Main St',
            city='New York',
            state='NY',
            zip_code='12345'
        )

    def test_user_update_success_email(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        user.email = 'new@user.com'
        user.save()
        self.assertEqual(user_model.objects.get(pID=123456789).email, 'new@user.com',
                         msg='User email should be updated')

    def test_user_update_success_password(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        user.set_password('bar')
        user.save()
        self.assertTrue(self.client.login(pID=123456789, password='bar'),
                        msg='Login with new password should succeed')

    def test_user_update_success_first_name(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        user.first_name = 'Jane'
        user.save()
        self.assertEqual(user_model.objects.get(pID=123456789).first_name, 'Jane',
                         msg='User first name should be updated')

    def test_user_update_success_last_name(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        user.last_name = 'Smith'
        user.save()
        self.assertEqual(user_model.objects.get(pID=123456789).last_name, 'Smith',
                         msg='User last name should be updated')

    def test_user_update_success_phone_number(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        user.phone_number = '0987654321'
        user.save()
        self.assertEqual(user_model.objects.get(pID=123456789).phone_number, '0987654321',
                         msg='User phone number should be updated')

    def test_user_update_success_address(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        user.address = '456 Main St'
        user.save()
        self.assertEqual(user_model.objects.get(pID=123456789).address, '456 Main St',
                         msg='User address should be updated')

    def test_user_update_success_city(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        user.city = 'Los Angeles'
        user.save()
        self.assertEqual(user_model.objects.get(pID=123456789).city, 'Los Angeles',
                         msg='User city should be updated')

    def test_user_update_success_state(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        user.state = 'CA'
        user.save()
        self.assertEqual(user_model.objects.get(pID=123456789).state, 'CA',
                         msg='User state should be updated')

    def test_user_update_success_zip_code(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        user.zip_code = '54321'
        user.save()
        self.assertEqual(user_model.objects.get(pID=123456789).zip_code, '54321',
                         msg='User zip code should be updated')

    def test_user_update_failure_email(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        with self.assertRaises(ValueError, msg='Email must be valid'):
            user.email = 'user'
            user.save()
        with self.assertRaises(ValueError, msg='Email must be set'):
            user.email = ''
            user.save()
        with self.assertRaises(ValueError, msg='Email must be set'):
            user.email = None
            user.save()

    def test_user_update_failure_password(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        with self.assertRaises(ValueError, msg='Password must be set'):
            user.set_password('')
            user.save()
        with self.assertRaises(ValueError, msg='Password must be set'):
            user.set_password(None)
            user.save()

    def test_user_update_failure_first_name(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        with self.assertRaises(ValueError, msg='First name must be set'):
            user.first_name = ''
            user.save()
        with self.assertRaises(ValueError, msg='First name must be set'):
            user.first_name = None
            user.save()

    def test_user_update_failure_last_name(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        with self.assertRaises(ValueError, msg='Last name must be set'):
            user.last_name = ''
            user.save()
        with self.assertRaises(ValueError, msg='Last name must be set'):
            user.last_name = None
            user.save()

    def test_user_update_failure_phone_number(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        with self.assertRaises(ValueError, msg='Phone number must be set'):
            user.phone_number = ''
            user.save()
        with self.assertRaises(ValueError, msg='Phone number must be set'):
            user.phone_number = None
            user.save()

    def test_user_update_failure_address(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        with self.assertRaises(ValueError, msg='Address must be set'):
            user.address = ''
            user.save()
        with self.assertRaises(ValueError, msg='Address must be set'):
            user.address = None
            user.save()

    def test_user_update_failure_city(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        with self.assertRaises(ValueError, msg='City must be set'):
            user.city = ''
            user.save()
        with self.assertRaises(ValueError, msg='City must be set'):
            user.city = None
            user.save()

    def test_user_update_failure_state(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        with self.assertRaises(ValueError, msg='State must be set'):
            user.state = ''
            user.save()
        with self.assertRaises(ValueError, msg='State must be set'):
            user.state = None
            user.save()

    def test_user_update_failure_zip_code(self):
        user_model = get_user_model()
        user = user_model.objects.get(pID=123456789)
        with self.assertRaises(ValueError, msg='Zip code must be set'):
            user.zip_code = ''
            user.save()
        with self.assertRaises(ValueError, msg='Zip code must be set'):
            user.zip_code = None
            user.save()
