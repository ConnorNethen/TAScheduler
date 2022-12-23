from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

import Scheduler
from Scheduler.classes.app_user import AppUserClass
from Scheduler.models import AppUser, Course
import Scheduler.classes.course



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
    if request.method =="POST":
        request.session['user'] = allUsers[int(request.POST['userNumber'])].pID
        return HttpResponseRedirect(reverse('userPage'))
    message = request.session.get("message")
    request.session.delete("message")
    if message == None:
        message = ""
    return render(request, "Scheduler/allUsers.html", {'userList': allUsers, 'message': message})

def user_view(request, userPID = ""):
    isUser = edit = False
    message = ""

    try:
        thisUser = AppUser.objects.get(pID=request.session.get('user'))
        thisUser = AppUserClass(thisUser.pID, thisUser.email, thisUser.password)
    except Exception:
        request.session['message'] = "Error Finding User's Page"
        return HttpResponseRedirect(reverse('All Users'))

    options = request.GET.get('options')
    if options == 'Delete':
        thisUser.removeAccount()
        return HttpResponseRedirect(reverse('index'), {"message": "User deleted Successfully"})
    elif options == 'Edit':
        edit = True

    if request.method == "POST":
        if not(request.POST['email'] == ""):
            thisUser.setEmail(request.POST['email'])
        else:
            message += " Email"
        if not (request.POST['street'] == ""):
            thisUser.setAddress(request.POST['street'])
        else:
            message += " Address"
        if not (request.POST['city'] == ""):
            thisUser.setCity(request.POST['city'])
        else:
            message += " City"
        if not (request.POST['state'] == ""):
            thisUser.setState(request.POST['state'])
        else:
            message += " State"
        if not (request.POST['zip'] == ""):
            thisUser.setZip(request.POST['zip'])
        else:
            message += " Zip Code"
        if message != "":
            message = "User Failed to Update Parameters:" + message
    #isAdmin = False
    #if thisUser.isAdmin():
    #   isAdmin = True
    #for clarity
    isAdmin = True
    #stop clarity

    return render(request, "Scheduler/userPage.html", {'user':thisUser,'edit': edit, 'isAdmin':isAdmin, 'isUser': isUser,'message': message})


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
