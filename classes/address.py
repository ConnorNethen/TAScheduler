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
