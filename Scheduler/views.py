from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

import Scheduler
from Scheduler.classes.app_user import AppUserClass
from Scheduler.models import AppUser, Course


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    if request.method == 'GET':
        return render(request, 'Scheduler/index.html')
    return  HttpResponseRedirect(reverse(request.POST['pageURL']))

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            request.session['email'] = email
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
    isUser = False
    message = ""
    try:
        pID = request.GET["pID"]
        thisUser = AppUser.objects.get(pID=pID)
        thisUser = AppUserClass(pID,thisUser.email,thisUser.password)
        if thisUser.getEmail() == request.session['email']:
            isUser == True
    except Exception:
        message = ""
        thisUser = AppUser.objects.get(email=request.session['email'])
        thisUser = AppUserClass(thisUser.pID,thisUser.email,thisUser.email)
        isUser = True
    try:
        options = request.GET['options']
        if options == 'Edit':
            edit = True
        elif options == 'Delete':
            thisUser.removeAccount()
            return HttpResponseRedirect(reverse('index'), {"message": "User deleted Successfully"})
    except Exception:
        edit = False
    if request.method == "POST":
        try:
            thisUser.setFirstName(request.POST['name'])
            thisUser.setEmail(request.POST['email'])
            thisUser.setAddress(request.POST['address'])
            thisUser.setCity(request.POST['city'])
            thisUser.setState(request.POST['state'])
            thisUser.setZip(request.POST['zip'])
        except Exception:
            message = "User Failed to Update a parameter!"
    #isAdmin = False
    #if thisUser.isAdmin():
    #   isAdmin = True
    #for clarity
    thisUser.setFullName("Christopher Faber")
    thisUser.setPhone("1234567890")
    thisUser.setAddress("6521 w mitchell st")
    thisUser.setCity("west allis")
    thisUser.setState("WI")
    thisUser.setZip("53214")
    isAdmin = True
    #stop clarity

    return render(request, "Scheduler/userPage.html", {'name':thisUser.getFullName(),'email': thisUser.getEmail(), 'phone':thisUser.getPhone(), 'street':thisUser.getAddress(), 'city':thisUser.getCity(), 'state':thisUser.getState(), 'zip':thisUser.getZip(), 'edit': edit, 'isAdmin':isAdmin, 'isUser': isUser,'message': message})