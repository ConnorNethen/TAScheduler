from Scheduler.models import User
from contactInfo import ContactInfo
from status import Status


class User:
    def __init__(
        self,
        pID,
        username,
        password,
        fname,
        lname,
        email,
        phone,
        street1,
        street2,
        city,
        state,
        zip,
        status,
    ):
        self.pID = pID
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state = state
        self.zip = zip
        self.status = status

    def save(self):
        contactInfo = ContactInfo(
            email=self.email,
            phone=self.phone,
            street1=self.street1,
            street2=self.street2,
            city=self.city,
            state=self.state,
            zip=self.zip,
        )
        contactInfo.save()

        User.objects.create(
            pID=self.pID,
            username=self.username,
            password=self.password,
            fname=self.fname,
            lname=self.lname,
            contactInfo=contactInfo,
            status=self.status,
        )
        return f"User {self.username} created successfully"

    # Getters
    def getFirstName(self):
        return self.fname

    def getLastName(self):
        return self.lname

    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phone

    def getStreet1(self):
        return self.street1

    def getStreet2(self):
        return self.street2

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getZip(self):
        return self.zip

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getStatus(self):
        return self.status

    # Setters
    def setPID(self, pID):
        self.pID = pID

    def setFirstName(self, fname):
        self.fname = fname

    def setLastName(self, lname):
        self.lname = lname

    def setEmail(self, email):
        self.email = email

    def setPhone(self, phone):
        self.phone = phone

    def setStreet1(self, street1):
        self.street1 = street1

    def setStreet2(self, street2):
        self.street2 = street2

    def setCity(self, city):
        self.city = city

    def setState(self, state):
        self.state = state

    def setZip(self, zip):
        self.zip = zip

    def setStatus(self, status):
        self.status = status

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password
