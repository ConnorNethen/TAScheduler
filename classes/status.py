from Scheduler.models import Status


class Status:
    def __init__(self, status):
        self.status = status

    def save(self):
        Status.objects.create(status=self.status)

    def setUniqueID(self):
        pass

    def setAdmin(self):
        pass

    def setInstructor(self):
        pass

    def setTA(self):
        pass

    def setUser(self):
        pass

    def getUniqueID(self):
        pass

    def getAdmin(self):
        pass

    def getInstructor(self):
        pass

    def getTA(self):
        pass

    def getUser(self):
        pass
