from django.test import TestCase, Client
from Scheduler.models import Course, AppUser


class LoginTest(TestCase):
    tester = None

    def setUp(self):
        tester = Client()
        AppUser("1234", "email@abc.com", "password", "first", "last",
                "0123456789", "123 w main st", "Milwaukee", "WI", "53211")
        # tester.post('/login/', {"username": "username", "password": "password"}, follow=True)

    def test_loginSuccess(self):
        tester = Client()
        response = tester.post('login/', {"email": "email@abc.com", "password": "password"}, follow=True)
        self.assertRedirects(response, 'userPage/')
        self.assertEqual(response.session["email"], "username", msg="Session key not equal to User's username")

    def test_incorrectUsername(self):
        tester = Client()
        response = tester.post('login/', {"email": "notUsername", "password": "password"}, follow=True)
        self.assertEqual(response.context["message"], "username or password incorrect, try again!",
                         msg="wrong username doesn't display the message username or password incorrect, try again!")

    def test_incorrectPassword(self):
        tester = Client()
        response = tester.post('login/', {"email": "email@abc.com", "password": "notPassword"}, follow=True)
        self.assertEqual(response.context["message"], "username or password incorrect, try again!",
                         msg="wrong password doesn't display the message username or password incorrect, try again!")
