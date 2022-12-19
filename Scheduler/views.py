from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


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


def createSection_view(request):
    if request.method == 'GET':
        return render(request, "Scheduler/createSection.html")
    if request.method == 'POST':
        courseNum = request.POST['courseID']
        sectionNum = request.POST['newSectionNumber']
        Scheduler.classes.section.__init__(courseNum, sectionNum)