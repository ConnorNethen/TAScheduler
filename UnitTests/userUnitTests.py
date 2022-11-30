from classes.user import User
import unittest
import Scheduler.models

class TestCreateAccount(unittest.TestCase):
    def test_successfulCreate(self):
        User.createAccount("jpmoyer", "jpmoyer@uwm.edu", "password", "James", "Moyer", "jpmoyer@uwm.edu", "T")
        userJames = Scheduler.models.User.objects.get(pID="jpmoyer")
        self.assertEqual(userJames.pID, "jpmoyer", msg="Panther ID not correct")
        self.assertEqual(userJames.username, "jpmoyer@uwm.edu", msg="Username not correct")
        self.assertEqual(userJames.password, "password", msg="Password not correct")
        self.assertEqual(userJames.fname, "James", msg="First name not correct")
        self.assertEqual(userJames.lname, "Moyer", msg="Last name not correct")
        self.assertEqual(userJames.contactInfo, "jpmoyer@uwm.edu", msg="Contact info not correct")
        self.assertEqual(userJames.status, "T", msg="Status not correct")

    def test_InvalidArg(self):
        with self.assertRaises(TypeError, msg="wrong Arg Type"):
            User.createAccount(User, "jpmoyer@uwm.edu", "password", "James", "Moyer", "jpmoyer@uwm.edu", "T")

    def test_oneArg(self):
        with self.assertRaises(TypeError, msg="Not enough arg"):
            User.createAccount("myPantherID")

    def test_twoArg(self):
        with self.assertRaises(TypeError, msg="Not enough arg"):
            User.createAccount("myPantherID", "myEmail@uwm.edu")

    def test_threeArg(self):
        with self.assertRaises(TypeError, msg="Not enough arg"):
            User.createAccount("myPantherID", "myEmail@uwm.edu", "first")

    def test_invalidName(self):
        User.createAccount("jlmoyer", "jlmoyer@uwm.edu", "password", "James", "Moyer", "jlmoyer@uwm.edu", "T")
        with self.assertRaises(KeyError, msg="Invalid key"):
            User.createAccount("jlmoyer", "anything@uwm.edu", "anything", "anything", "anything", "anything@uwm.edu", "T")



class TestDeleteAccount(unittest.TestCase):
    def test_successfulDelete(self):
        #create a user manually in the database with pID jkmoy
        Scheduler.models.User(pID="jkmoy", username="jkmoy@uwm.edu", password="myPass", fname="James", lname="Moyer", contactInfo="jkmoy@uwm.edu", status="T")
        User.deleteAccount("jkmoy")
        self.assertEqual(Scheduler.models.User.objects.get(pID="jkmoy"), None, msg="Primary key was found")

    def test_invalidArg(self):
        with self.assertRaises(TypeError, msg="Wrong arg type"):
            User.deleteAccount(User)
