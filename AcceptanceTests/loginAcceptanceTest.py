from django.test import TestCase, Client
from Scheduler.models import User, ContactInfo, Address

class LoginTest(TestCase):
    tester = null

    def setup(self):

        User(1234, username, password, first, last,ContactInfo("email@abc.com" , "123456789", Address("street1", "street2" , "city", "state", "12345")))

    def test_loginSuccess(self):

        pass
    def test_incorrectUsername(self):
        pass
    def test_incorrectPassword(self):
        pass
