from django.shortcuts import render, redirect
from django.views import View
from Scheduler.models import User


class Login(View):
    def get(self, request):
        return render(request, "login.html", {"message": None})

    def post(self, request):
        validCred = True
        myUsername = request.POST['username']
        myPassword = request.POST['password']
        bad_user = False
        bad_password = False

        try:
            user = User.objects.get(name=myUsername)
            bad_password = (user.password != myPassword)
        except:
            bad_user = True

        if bad_user or bad_password:
            validCred = False

        if validCred:
            request.session["username"] = myUsername
            return redirect("/index/")
        else:
            return render(request, "login.html", {"message": "Username or password is incorrect, try again!"})
