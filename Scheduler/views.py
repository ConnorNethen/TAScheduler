from django.shortcuts import render, redirect
from django.views import View
from Scheduler.models import User, ContactInfo
from classes.course import Course
from classes.section import Section
from classes.user import User


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
            request.session["pID"] = myUsername
            return redirect("/index/")
        else:
            return render(request, "Lhtml", {"message": "Username or password is incorrect, try again!"})


class Index(View):
    def get(self, request):
        return render(request, "index.html", {"message": None})

    def post(self, request):
        path = request.POST['Submit']
        if self.isAdminPath(path) and (not self.isAdmin(request.Session["username"])):
            return render(request, "index.html", {"message": "Access Denied"})
        return redirect(path)

    def isAdminPath(self, path):
        for i in self.urlpatters:
            if path == i.__str__():
                return True

    def isAdmin(self, username):
        if username.Status() == "A":
            return True
        return False


class CreateUser(View):
    def get(self, request):
        return render(request, "users_new.html", {"message": request.GET["message"]})

    def post(self, request):
        ContactInfo(request.POST["email"], request.POST["number"], )
        message = User.createAccount(request.POST["pID"], request.POST["username"], request.post["password"],
                                     request.POST["fname"], request.POST["lname"], request.POST["email"],
                                     request.post["status"])
        if message == "":
            return redirect('index/', {"message": message})
        return render(request, "users_new.html", {"message": "Account Created Successfully"})


class CreateCourse(View):
    def get(self, request):
        return render(request, "course_new.html", {"message": request.GET["message"]})

    def post(self, request):
        message = Course.createCourse(request.POST["courseNumber"], request.POST["semester"], request.POST["year"])
        for section in request.POST["sections"]:
            message += Section.createSection(section[0], section[1], section[2], section[3])
        if message == "":
            return redirect("index/", {"message": "Course created Succesfully"})
        return render(request, "course_new.html", {"message": message})


class UserPage(View):
    def get(self, request):
        myUser = User.objects.get(pID=request.GET["userPID"])
        mySections = Section.getSections(myUser.pID)
        myCourses = Course.getCourses(myUser.pID)
        return render(request, "user.html",
                      {"user": myUser, "sections": mySections, "courses": myCourses, "message": request.GET["message"]})

    def post(self, request):
        path = request.POST["Submit"]
        myPID = request.Session["pID"]
        userPID = request.POST["userPID"]
        if ((not User.isUser(myPID, userPID)) and (not User.isAdmin(myPID)) and (str(path) == "users/edit")):
            return render(request, "user.html", {"message": "Access Denied"})
        return redirect(path)


class AllUsers(View):
    def get(self, request):
        allUsers = User.objects.all()
        return render(request, "users.html", {"message": request.GET["message"], "users": allUsers})

    def post(self, request):
        path = request.POST["Submit"]
        if (not User.isAdmin(request.Session["pID"]) and (path == "user/new/")):
            return render(request, "users.html", {"message": "Access Denied"})
        if path[:10] == "users/user":
            return redirect(path, {"userPID": path[10:]})
        return redirect(path)


class UserEdit(View):
    def get(self, request):
        pass

    def post(self, request):
        myPID = request.Session["pID"]
        userPID = request.POST["userPID"]
        option = request.POST["submit"]
        message = ""
        if (not User.isAdmin(myPID)) and (not User.isUser(myPID, userPID)):
            message = "Don't have access to edit this user"
        if User.isAdmin(myPID):
            if option == "delete" and User.isUSer(myPID, userPID):
                return render(request, "user_edit.html", {"message": "Can't Delete your own Account"})
            elif option == "delete" and User.deleteAccount(userPID):
                return redirect("index/", {"message": "Account Succesfully Deleted"})
            else:
                return render(request, "user.html", {"message": "Account didnt delete"})
            editAccount(request.POST["fname"], request.POST["lname"], request.POST["username"],
                        request.POST["password"], request.POST["email"], request.post["phone"], request.POST["address"],
                        reqest.POST["status"])
            message = "user updated successfully"
        elif User.isUser(myPID, userPID):
            User.editAccount(None, None, None, None, request.POST["email"], request.post["phone"], request.POST["address"],
                        None)
            message = "user updated succesfully"
        return redirect("users/user/" + userPID, {"message": message})
