from Scheduler.models import Address


class Address:
    def __init__(self, street1, street2, city, state, zip):
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state = state
        self.zip = zip

    def save(self):
        Address.objects.create(
            street1=self.street1,
            street2=self.street2,
            city=self.city,
            state=self.state,
            zip=self.zip,
        )

    def setStreet1(self):
        pass

    def setStreet2(self):
        pass

    def setCity(self):
        pass

    def setState(self):
        pass

    def setZip(self):
        pass

    def setContactInfo(self):
        pass

    def getUniqueID(self):
        pass

    def getStreet1(self):
        pass

    def getStreet2(self):
        pass

    def getCity(self):
        pass

    def getState(self):
        pass

    def getZip(self):
        pass

    def getContactInfo(self):
        pass
