from django.db import models

# Create your models here.
class Address(models.Model):
    street1 = models.CharField(max_length=100)
    street2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.USStateField()
    zip = models.CharField(max_length=5)

    def __str__(self):
        return self.street1 + ", " + self.city + ", " + self.state + " " + self.zip


class ContactInfo(models.Model):
    email = models.EmailField(max_length=100)
    phone = models.PhoneNumberField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Status(models.Model):
    STATUS = (("Admin", "Admin"), ("Instructor", "Instructor"), ("TA", "TA"))
    status = models.CharField(max_length=1, choices=STATUS)


class AppUser(models.Model):
    pID = models.CharField(max_length=50, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    contactInfo = models.ForeignKey(ContactInfo, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


class Course(models.Model):
    number = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.number + " - " + self.name


class Section(models.Model):
    number = models.CharField(max_length=3, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    time = models.CharField(max_length=50)


class UserToSection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
