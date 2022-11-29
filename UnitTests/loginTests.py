import unittest
from classes.login import Login
from Scheduler.models import Login


class TestLoginInit(unittest.TestCase):
    database = None

    def setUp(self):
        self.database = {"one": "onePass", "two": "twoPass"}

        for i in self.database:
            temp = Login(name=i.keys(), password=i.values())
            temp.save()

    def test_correctName(self):
        for i in self.database:
            resp = self.monkey.post("/", {"name": i.keys(), "password": i.values()}, follow=True)
            self.assertEqual(resp.context["name"], i.keys(), "name not passed from login to list")


class LoginFail(unittest.TestCase):
    database = None

    def setUp(self):
        self.database = {"one": "onePass", "two": "twoPass"}

        for i in self.database:
            temp = Login(name=i.keys(), password=i.values())
            temp.save()

    def test_noPass(self):
        for i in self.database:
            resp = self.monkey.post("/", {"name": i.keys(), "password": ""}, follow=True)
            self.assertEqual(resp.context["message"], "bad password")

    def test_BadPass(self):
        for i in self.thingList.keys():
            resp = self.monkey.post("/", {"name": i.keys, "password": "wrong"}, follow=True)
            self.assertEqual(resp.context["message"], "bad password")

