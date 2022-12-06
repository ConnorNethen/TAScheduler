from Scheduler.models import ContactInfo
from address import Address

class ContactInfo():
    def __init__(self, email, phone, street1, street2, city, state, zip):
        self.email = email
        self.phone = phone
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state = state
        self.zip = zip

    def save(self):
        address = Address(street1=self.street1, street2=self.street2, city=self.city, state=self.state, zip=self.zip)
        address.save()
        ContactInfo.objects.create(email=self.email, phone=self.phone, address=address)

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