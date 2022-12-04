from django.test import TestCase, Client
from Scheduler.models import User, ContactInfo, Address

class LoginTest(TestCase):
    tester = null

    def setup(self):
        tester = Client()
        User("1234", "username", "password", "first", "last",
             ContactInfo("email@abc.com", "123456789", Address("street1", "street2", "city", "state", "12345")),
             Status("A"))
        tester.post('/login/', {"username": "username", "password": "password"}, follow=true)
    def test_loginSuccess(self):
        response = tester.post('/login/', {"username": "username", "password": "password"}, follow= true)
        self.assertRedircts(response, 'index', msg= "Did not redirect to home page")
        self.assertEqual(response.session["username"], "username", msg= "Session key not equal to User's username")
    def test_incorrectUsername(self):
        response = tester.post('/login/', {"username": "notUsername", "password": "password"}, follow=true)
        self.assertEqual(response.context["message"], "username or password incorrect, try again!", msg="wrong username doesn't display the message username or password incorrect, try again!")
    def test_incorrectPassword(self):
        response = tester.post('/login/', {"username": "username", "notPassword": "password"}, follow=true)
        self.assertEqual(response.context["message"], "username or password incorrect, try again!", msg="wrong password doesn't display the message username or password incorrect, try again!")
