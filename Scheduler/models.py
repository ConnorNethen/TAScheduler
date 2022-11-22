from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.street + ", " + self.city + ", " + self.state + " " + self.zip


class ContactInfo(models.Model):
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Status(models.Model):
    status = models.CharField(max_length=100)


class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    pID = models.CharField(max_length=50)
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    contactInfo = models.ForeignKey(ContactInfo, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


class Course(models.Model):
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.number + " - " + self.name


class Section(models.Model):
    number = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    time = models.CharField(max_length=50)


class UserToSection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
