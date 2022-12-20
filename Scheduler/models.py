from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import AppUserManager


# Create your models here.
class AppUser(AbstractBaseUser, PermissionsMixin):
    pID = models.CharField(_('panther ID'), max_length=9, primary_key=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    phone = models.CharField(_('phone number'), max_length=10, blank=True)
    address = models.CharField(_('address'), max_length=100, blank=True)
    city = models.CharField(_('city'), max_length=50, blank=True)
    state = models.CharField(_('state'), max_length=2, blank=True)
    zip_code = models.CharField(_('zip code'), max_length=5, blank=True)
    courses = models.ManyToManyField('Course', through='UserCourse', related_name='users')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['pID']

    objects = AppUserManager()

    def __str__(self):
        return self.email


class Course(models.Model):
    SEMESTER_CHOICES = (
        ('F', 'Fall'),
        ('S', 'Spring'),
        ('U', 'Summer'),
        ('W', 'Winter'),
    )
    courseID = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES)
    year = models.IntegerField()

    def __str__(self):
        return self.courseID


class Section(models.Model):
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    sectionID = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return self.sectionID


class UserCourse(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email + " " + self.course.courseID + " " + self.role