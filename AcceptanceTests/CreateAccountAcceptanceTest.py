from django.test import TestCase, Client
from Scheduler.models import AppUser


class CreateAccount(TestCase):
    tester = None

    def setUp(self):
        self.tester = Client()
        AppUser("1234", "email@abc.com", "password", "first", "last",
                "0123456789", "123 w main st", "Milwaukee", "WI", "53211")

    def test_UserCreationSuccess(self):
        # tester = Client()
        self.tester.post('/login/', {"email": "email@abc.com", "password": "password"}, follow=True)
        self.tester.post('/index/', {"Submit": "'createUser/'"}, follow=True)
        self.tester.post('createUser/',
                         {"newPantherID": "pantherID", "newEmail": "myEmail@abc.com", "newPassword": "password",
                          "newFirstName": "fName", "newLastName": "lName", "newPhone": "0123456789",
                          "newAddress": "myStreet", "newCity": "myCity", "newState": "myState", "newZip": "12345"})
        userTest = AppUser.objects.get(pID="pantherID")
        self.assertEquals(userTest.pID, "pantherID", msg="pID isn't pantherID")
        self.assertEquals(userTest.email, "myEmail@abc.com", msg="email isn't myEmail@abc.com")
        self.assertEquals(userTest.password, "myPassword", msg="password isn't myPassword")
        self.assertEquals(userTest.first_name, "fName", msg="first_name isn't fName")
        self.assertEquals(userTest.last_name, "lName", msg="last_name isn't lName")
        self.assertEquals(userTest.phone_number, "0123456789", msg="phone_number isn't 0123456789")
        self.assertEquals(userTest.address, "myStreet", msg="address isn't myStreet")
        self.assertEquals(userTest.city, "myCity", msg="city isn't myCity")
        self.assertEquals(userTest.state, "myState", msg="state isn't myState")
        self.assertEquals(userTest.zip, "12345", msg="zip isn't 12345")
        self.assertRedirects('index/')

    def test_pIDExists(self):
        # tester = Client()
        self.tester.post('/login/', {"email": "username", "password": "password"}, follow=True)
        self.tester.post('/index/', {"Submit": "'createUser/'"}, follow=True)
        resp = self.tester.post('createUser/',
                                {"pID": "pantherID", "email": "myEmail@abc.com", "password": "myPassword",
                                 "first_name": "fName", "last_name": "lName", "phone_number": "0123456789",
                                 "address": "myStreet", "city": "myCity", "state": "myState", "zipCode": "12345"})
        self.assertEquals(resp.context["message"], "pID already exists",
                          msg="pID already exists, and message didnt populate")
        self.assertEquals(AppUser.objects.all().count, 1, msg="user was created when it shouldn't have been.")

    def test_EmailExists(self):
        # tester = Client()
        self.tester.post('/login/', {"email": "username", "password": "password"}, follow=True)
        self.tester.post('/index/', {"Submit": "'createUser/'"}, follow=True)
        resp = self.tester.post('createUser/',
                                {"pID": "pantherID", "email": "myEmail@abc.com", "password": "myPassword",
                                 "first_name": "fName", "last_name": "lName", "phone_number": "0123456789",
                                 "address": "myStreet", "city": "myCity", "state": "myState", "zipCode": "12345"})
        self.assertEquals(resp.context["message"], "email already exists",
                          msg="email already exists, and message didnt populate")
        self.assertEquals(AppUser.objects.all().count, 1, msg="user was created when it shouldn't have been.")

    def test_PhoneNumberExists(self):
        # tester = Client()
        self.tester.post('/login/', {"email": "username", "password": "password"}, follow=True)
        self.tester.post('/index/', {"Submit": "'createUser/'"}, follow=True)
        resp = self.tester.post('createUser/',
                                {"pID": "pantherID", "email": "myEmail@abc.com", "password": "myPassword",
                                 "first_name": "fName", "last_name": "lName", "phone_number": "0123456789",
                                 "address": "myStreet", "city": "myCity", "state": "myState", "zipCode": "12345"})
        self.assertEquals(resp.context["message"], "phone number already exists",
                          msg="phone number already exists, and message didnt populate")
        self.assertEquals(AppUser.objects.all().count, 1, msg="user was created when it shouldn't have been.")

    # def test_InstructorAccess(self):
    #     tester = Client()
    #     User("123456I", "usernameIN", "passwordIN", "firstIN", "lastIN",
    #          ContactInfo("emailIN@abc.com", "123456781", Address("street1", "street2", "city", "state", "12345")),
    #          Status("I"))
    #     tester.post('/login/', {"username": "usernameIN", "password": "passwordIN"}, follow=True)
    #     resp = tester.post('/index/', {"Submit": "'users/new/'"}, follow=True)
    #     self.assertEquals(resp.context["message"], "Access Denied",
    #                       msg="Instructor status attempted access create course page, and message didnt populate")
    #
    # def test_TAAccess(self):
    #     tester = Client()
    #     User("123456TA", "usernameTA", "passwordTA", "firstTA", "lastTA",
    #          ContactInfo("emailTA@abc.com", "123456781", Address("street1", "street2", "city", "state", "12345")),
    #          Status("T"))
    #     tester.post('/login/', {"username": "usernameTA", "password": "passwordTA"}, follow=True)
    #     resp = tester.post('/index/', {"Submit": "'users/new/'"}, follow=True)
    #     self.assertEquals(resp.context["message"], "Access Denied",
    #                       msg="TA status attempted access create course page, and message didnt populate")
