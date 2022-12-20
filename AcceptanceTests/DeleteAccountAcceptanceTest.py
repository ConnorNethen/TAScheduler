from django.test import TestCase, Client
from Scheduler.models import Course, UserCourse, Section, AppUser


class DeleteAccount(TestCase):
    tester = None

    def setup(self):
        Address("street1", "street2", "city", "state", "12345")
        User("1234", "username", "password", "first", "last",
             ContactInfo("email@abc.com", "123456789", "street1"),
             Status("A"))
        User("123456TA", "usernameTA", "passwordTA", "firstTA", "lastTA",
             ContactInfo("emailTA@abc.com", "123456781", "street1"),
             Status("T"))

    def test_successfulDeletion(self):
        tester = Client()
        response = tester.post('login/', {"username": "username", "password": "password"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        response = tester.post('index', {"Submit": "users/"}, follow=True)
        self.assertRedircts(response, 'users/', msg="Did not redirect to the all users page")
        response = tester.post('users/', {"Submit": "users/user/123456TA"}, follow=True)
        self.assertRedircts(response, 'users/user/123456TA', msg="Did not redirect to the all users page")
        response = tester.post('users/user/123456TA', {"Submit": "'users/user/123456TA/edit/'"}, follow=True)
        self.assertRedircts(response, 'users/user/123456TA/edit/', msg="Did not redirect to user edit page")
        response = tester.post('users/user/123456TA', {"Submit": "delete"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        self.assertEqual(response.context["message"], "Account Successfully Deleted")
        self.assertEqual(User.objects.all().count(), 1, msg="User not deleted out of database")

    def test_adminDeleteItself(self):
        tester = Client()
        response = tester.post('login/', {"username": "username", "password": "password"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        response = tester.post('index', {"Submit": "users/"}, follow=True)
        self.assertRedircts(response, 'users/', msg="Did not redirect to the all users page")
        response = tester.post('users/', {"Submit": "users/user/123456TA"}, follow=True)
        self.assertRedircts(response, 'users/user/1234', msg="Did not redirect to the all users page")
        response = tester.post('users/user/1234', {"Submit": "'users/user/1234/edit/'"}, follow=True)
        self.assertRedircts(response, 'users/user/1234/edit/', msg="Did not redirect to user edit page")
        response = tester.post('users/user/1234', {"Submit": "delete"}, follow=True)
        self.assertEqual(response.context["message"], "User can not delete itself",
                         msg="error message didnt populate when User tried to delete itself")

    def test_TADeletion(self):
        tester = Client()
        response = tester.post('login/', {"username": "usernameTA", "password": "passwordTA"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        response = tester.post('index', {"Submit": "users/"}, follow=True)
        self.assertRedircts(response, 'users/', msg="Did not redirect to the all users page")
        response = tester.post('users/', {"Submit": "users/user/1234"}, follow=True)
        self.assertRedircts(response, 'users/user/1234', msg="Did not redirect to the all users page")
        response = tester.post('users/user/1234', {"Submit": "'users/user/1234/edit/'"}, follow=True)
        self.assertRedircts(response, 'users/user/1234/edit/', msg="Did not redirect to user edit page")
        response = tester.post('users/user/1234', {"Submit": "delete"}, follow=True)
        self.assertEqual(response.context["message"], "User can not delete Accounts",
                         msg="error message didnt populate when TA tried to delete an account")

    def test_InstructorDeletion(self):
        tester = Client()
        User("123456IN", "usernameIN", "passwordIN", "firstIN", "lastIN",
             ContactInfo("emailTA@abc.com", "123456781", "street1"),
             Status("I"))
        response = tester.post('login/', {"username": "usernameIN", "password": "passwordIN"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        response = tester.post('index', {"Submit": "users/"}, follow=True)
        self.assertRedircts(response, 'users/', msg="Did not redirect to the all users page")
        response = tester.post('users/', {"Submit": "users/user/1234"}, follow=True)
        self.assertRedircts(response, 'users/user/1234', msg="Did not redirect to the all users page")
        response = tester.post('users/user/1234', {"Submit": "'users/user/1234/edit/'"}, follow=True)
        self.assertRedircts(response, 'users/user/1234/edit/', msg="Did not redirect to user edit page")
        response = tester.post('users/user/1234', {"Submit": "delete"}, follow=True)
        self.assertEqual(response.context["message"], "User can not delete Accounts",
                         msg="error message didnt populate when Instructor tried to delete an account")
