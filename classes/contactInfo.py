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

    def setAddress(self, address):
        self.address = address
        
    def getUniqueID(self):
        pass

    def getEmail(self):
        pass

    def getPhone(self):
        pass

    def getAddress(self):
        pass

    def getUser(self):
        pass

