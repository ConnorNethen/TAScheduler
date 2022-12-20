from django.test import TestCase, Client
from Scheduler.models import Course, UserCourse, Section, AppUser


class CreateAccount(TestCase):
    tester = None

    def setUp(self):
        tester = Client()
        User("1234", "username", "password", "first", "last",
             ContactInfo("email@abc.com", "123456789", Address("street1", "street2", "city", "state", "12345")),
             Status("A"))

    def test_UserCreationSuccess(self):
        tester = Client()
        tester.post('/login/', {"username": "username", "password": "password"}, follow=True)
        tester.post('/index/', {"Submit": "'users/new/'"}, follow=True)
        tester.post('users/new/',
                    {"pID": "pantherID", "email": "myEmail@abc.com", "password": "myPassword", "firstName": "fName",
                     "lastName": "lName", "phoneNumber": "123456789", "street1": "myStreet", "street2": "myStreet2",
                     "city": "myCity", "state": "myState", "zipCode": "12345", "status": "T"})
        userTest = User.get("pantherID")
        self.assertEquals(userTest.username, "myEmail@abc.com", msg="username isnt myEmail@abc.com")
        self.assertEquals(userTest.password, "myPassword", msg="password isnt myPassword")
        self.assertEquals(userTest.fname, "fName", msg="firstName isnt fName")
        self.assertEquals(userTest.lname, "lName", msg="lastName isnt lName")
        self.assertEquals(userTest.ContactInfo.email, "email", msg="username isnt myEmail@abc.com")
        self.assertEquals(userTest.ContactInfo.phone, "123456789", msg="phoneNumber isnt 123456789")
        self.assertEquals(userTest.ContactInfo.Address.street1, "myStreet", msg="street1 isn't myStreet")
        self.assertEquals(userTest.ContactInfo.Address.street2, "myStreet2", msg="street2 isn't myStreet2")
        self.assertEquals(userTest.ContactInfo.Address.city, "myCity", msg="city isn't myCity")
        self.assertEquals(userTest.ContactInfo.Address.state, "myState", msg="state isn't myState")
        self.assertEquals(userTest.ContactInfo.Address.city, "myCity", msg="city isn't myCity")
        self.assertEquals(userTest.ContactInfo.Address.zip, "12345", msg="zip isn't 12345")
        self.assertEquals(userTest.ContactInfo.Address.status, "T", msg="status isn't T")
        self.assertRedircts('index/')

    def test_pIDExists(self):
        tester = Client()
        tester.post('/login/', {"username": "username", "password": "password"}, follow=True)
        tester.post('/index/', {"Submit": "'users/new/'"}, follow=True)
        resp = tester.post('users/new/',
                           {"pID": "1234", "email": "myEmail@abc.com", "password": "myPassword", "firstName": "fName",
                            "lastName": "lName", "phoneNumber": "123456789", "street1": "myStreet",
                            "street2": "myStreet2",
                            "city": "myCity", "state": "myState", "zipCode": "12345", "status": "T"})
        self.assertEquals(resp.context["message"], "pID already exists",
                          msg="pID already exists, and message didnt populate")
        self.assertEquals(User.objects.all().count, 1, msg="user was created when it shouldn't have been.")

    def test_EmailExists(self):
        tester = Client()
        tester.post('/login/', {"username": "username", "password": "password"}, follow=True)
        tester.post('/index/', {"Submit": "'users/new/'"}, follow=True)
        resp = tester.post('users/new/',
                           {"pID": "pantherID", "email": "email@abc.com", "password": "myPassword",
                            "firstName": "fName",
                            "lastName": "lName", "phoneNumber": "123456789", "street1": "myStreet",
                            "street2": "myStreet2",
                            "city": "myCity", "state": "myState", "zipCode": "12345", "status": "T"})
        self.assertEquals(resp.context["message"], "email already exists",
                          msg="email already exists, and message didnt populate")
        self.assertEquals(User.objects.all().count, 1, msg="user was created when it shouldn't have been.")

    def test_PhoneNumberExists(self):
        tester = Client()
        tester.post('/login/', {"username": "username", "password": "password"}, follow=True)
        tester.post('/index/', {"Submit": "'users/new/'"}, follow=True)
        resp = tester.post('users/new/',
                           {"pID": "pantherID", "email": "myEmail@abc.com", "password": "myPassword",
                            "firstName": "fName",
                            "lastName": "lName", "phoneNumber": "123456789", "street1": "myStreet",
                            "street2": "myStreet2",
                            "city": "myCity", "state": "myState", "zipCode": "12345", "status": "T"})
        self.assertEquals(resp.context["message"], "phone number already exists",
                          msg="phone number already exists, and message didnt populate")
        self.assertEquals(User.objects.all().count, 1, msg="user was created when it shouldn't have been.")

    def test_InstructorAccess(self):
        tester = Client()
        User("123456I", "usernameIN", "passwordIN", "firstIN", "lastIN",
             ContactInfo("emailIN@abc.com", "123456781", Address("street1", "street2", "city", "state", "12345")),
             Status("I"))
        tester.post('/login/', {"username": "usernameIN", "password": "passwordIN"}, follow=True)
        resp = tester.post('/index/', {"Submit": "'users/new/'"}, follow=True)
        self.assertEquals(resp.context["message"], "Access Denied",
                          msg="Instructor status attempted access create course page, and message didnt populate")

    def test_TAAccess(self):
        tester = Client()
        User("123456TA", "usernameTA", "passwordTA", "firstTA", "lastTA",
             ContactInfo("emailTA@abc.com", "123456781", Address("street1", "street2", "city", "state", "12345")),
             Status("T"))
        tester.post('/login/', {"username": "usernameTA", "password": "passwordTA"}, follow=True)
        resp = tester.post('/index/', {"Submit": "'users/new/'"}, follow=True)
        self.assertEquals(resp.context["message"], "Access Denied",
                          msg="TA status attempted access create course page, and message didnt populate")
