from Scheduler.models import AppUser


class AppUserClass:
    pID = None
    email = None
    password = None
    first_name = None
    last_name = None
    phone_number = None
    address = None
    city = None
    state = None
    zip_code = None

    def __init__(self, pID="", email="", password="", first_name="", last_name="",
                 phone_number="", address="", city="", state="", zip_code=""):
        # check if user exists first
        try:
            user = AppUser.objects.get(pID=pID)
            self.pID = user.pID
            self.email = user.email
            self.password = user.password
            self.first_name = user.first_name
            self.last_name = user.last_name
            self.phone_number = user.phone_number
            self.address = user.address
            self.city = user.city
            self.state = user.state
            self.zip_code = user.zip_code

        except Exception:
            # need to make a new user
            if pID == "" or email == "" or password == "":
                raise TypeError("Must pass pID, email, and password")
            else:
                user = AppUser(pID=pID, email=email, password=password, first_name=first_name, last_name=last_name,
                               phone=phone_number, address=address, city=city, state=state, zip_code=zip_code)
                user.save()
                self.pID = pID
                self.email = email
                self.password = password
                self.first_name = first_name
                self.last_name = last_name
                self.phone_number = phone_number
                self.address = address
                self.city = city
                self.state = state
                self.zip_code = zip_code

    def getPID(self):
        if self.pID == "":
            raise TypeError("No pID assigned to user.")
        else:
            return self.pID

    def getEmail(self):
        if self.email == "":
            raise TypeError("No email assigned to user.")
        else:
            return self.email

    def setEmail(self, email):
        try:
            user = AppUser.objects.get(pID=self.pID)
            user.email = email
            self.email = email
            user.save()
        except Exception:
            return TypeError("Invalid email")

    def getFirstName(self):
        if self.first_name == "":
            raise TypeError("No first name assigned to user.")
        else:
            return self.first_name

    def setFirstName(self, name):
        user = AppUser.objects.get(pID=self.pID)
        user.first_name = name
        self.first_name = name
        user.save()

    def getLastName(self):
        if self.last_name == "":
            raise TypeError("No last name assigned to user.")
        else:
            return self.last_name

    def setLastName(self, name):
        user = AppUser.objects.get(pID=self.pID)
        user.last_name = name
        self.last_name = name
        user.save()

    def getFullName(self):
        name = self.first_name + " " + self.last_name
        if name == " ":
            return TypeError("User does not have a name.")
        return name

    def setFullName(self, name):
        words = name.split()
        if len(words) != 2:
            return TypeError("Invalid name")
        user = AppUser.objects.get(pID=self.pID)
        user.first_name = words[0]
        user.last_name = words[1]
        self.first_name = words[0]
        self.last_name = words[1]
        user.save()

    def getPhone(self):
        if self.phone_number == "":
            raise TypeError("No phone number assigned to user.")
        else:
            return self.phone_number

    def setPhone(self, phone):
        user = AppUser.objects.get(pID=self.pID)
        user.phone = phone
        self.phone_number = phone
        user.save()

    def getAddress(self):
        if self.address == "":
            raise TypeError("No address assigned to user.")
        else:
            return self.address

    def setAddress(self, address):
        user = AppUser.objects.get(pID=self.pID)
        user.address = address
        self.address = address
        user.save()

    def getCity(self):
        if self.city == "":
            raise TypeError("No city assigned to user.")
        else:
            return self.city

    def setCity(self, city):
        user = AppUser.objects.get(pID=self.pID)
        user.city = city
        self.city = city
        user.save()

    def getState(self):
        if self.state == "":
            raise TypeError("No state assigned to user.")
        else:
            return self.state

    def setState(self, state):
        user = AppUser.objects.get(pID=self.pID)
        user.state = state
        self.state = state
        user.save()

    def getZip(self):
        if self.zip_code == "":
            raise TypeError("No zip code assigned to user.")
        else:
            return self.zip_code

    def setZip(self, zip):
        user = AppUser.objects.get(pID=self.pID)
        user.zip_code = zip
        self.zip_code = zip
        user.save()

    def getCourses(self):
        pass

    def addCourse(self, courseID):
        pass

    def removeCourse(self, courseID):
        pass

    def getSections(self):
        pass

    def addSection(self, sectionID):
        pass

    def removeSection(self, sectionID):
        pass

    def removeAccount(self):
        pass
