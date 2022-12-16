from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'Scheduler/index.html')


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
    pass


def createUser_view(request):
    pass
