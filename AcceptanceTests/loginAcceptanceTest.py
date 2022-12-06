from django.test import TestCase, Client
from Scheduler.models import User, ContactInfo, Address, Status


class LoginTest(TestCase):
    tester = None

    def setup(self):
        tester = Client()
        User("1234", "username", "password", "first", "last",
             ContactInfo("email@abc.com", "123456789", Address("street1", "street2", "city", "state", "12345")),
             Status("A"))
        tester.post('/login/', {"username": "username", "password": "password"}, follow=True)

    def test_loginSuccess(self):
        tester = Client()
        response = tester.post('/login/', {"username": "username", "password": "password"}, follow=True)
        self.assertRedircts(response, 'index', msg="Did not redirect to home page")
        self.assertEqual(response.session["username"], "username", msg="Session key not equal to User's username")

    def test_incorrectUsername(self):
        tester = Client()
        response = tester.post('/login/', {"username": "notUsername", "password": "password"}, follow=True)
        self.assertEqual(response.context["message"], "username or password incorrect, try again!",
                         msg="wrong username doesn't display the message username or password incorrect, try again!")

    def test_incorrectPassword(self):
        tester = Client()
        response = tester.post('/login/', {"username": "username", "notPassword": "password"}, follow=True)
        self.assertEqual(response.context["message"], "username or password incorrect, try again!",
                         msg="wrong password doesn't display the message username or password incorrect, try again!")
