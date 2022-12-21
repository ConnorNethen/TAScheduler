from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

import Scheduler.classes.course


import Scheduler
from Scheduler.models import Course, AppUser


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    if request.method == 'GET':
        return render(request, 'Scheduler/index.html')
    return HttpResponseRedirect(reverse(request.POST['pageURL']))


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'Scheduler/login.html', {
                'error': 'Invalid email or password'
            })
    return render(request, 'Scheduler/login.html')


def logout_view(request):
    logout(request)
    return render(request, "Scheduler/login.html", {
        'message': "Logged out"
    })


def createCourse_view(request):
    if request.method == 'GET':
        return render(request, "Scheduler/createCourses.html")
    if request.method == 'POST':
        courseNum = request.POST['newCourseID']
        courseName = request.POST['newCourseName']
        courseSemester = request.POST['newSemester']
        courseYear = request.POST['newYear']
        Scheduler.classes.course.AppCourse.__init__(courseNum, courseName, courseSemester, courseYear)


def createUser_view(request):
    if request.method == 'GET':
        return render(request, "Scheduler/createUser.html")
    if request.method == 'POST':
        pID = request.POST['newPantherID']
        email = request.POST['newEmail']
        password = request.POST['newPassword']
        phone = request.POST['newPhone']
        firstName = request.POST['newFirstName']
        lastName = request.POST['newLastName']
        address = request.POST['newAddress']
        city = request.POST['newCity']
        state = request.POST['newState']
        zipCode = request.POST['newZip']
        Scheduler.classes.app_user.__init__(pID, email, password, firstName, lastName, phone, address, city, state, zipCode)


def allCourses_view(request):
    allAppCourse = []
    allCourses = Course.objects.all()
    for i in allCourses:
        allAppCourse.append(Scheduler.classes.course.AppCourse(i))
    return render(request, "Scheduler/allCourses.html", {'courseList': allAppCourse})


def allUsers_view(request):
    allUsers = AppUser.objects.all()
    return render(request, "Scheduler/allUsers.html", {'userList': allUsers})


def user_view(request):
    allUsers = AppUser.objects.all()
    return render(request, "Scheduler/allCourses.html", {'userList': allUsers})

