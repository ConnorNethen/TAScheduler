from Scheduler.models import Course, Section

class Section:
    def __init__(self, number, course, type, time):
        self.number = number
        self.course = course
        self.type = type
        self.time = time

    def save(self):
        Section.objects.create(
            number=self.number,
            course=self.course,
            type=self.type,
            time=self.time,
        )
        return f"Section {self.number} created successfully"

    def getNumber(self):
        return self.number

    def getCourse(self):
        return self.course

    def getType(self):
        return self.type

    def getTime(self):
        return self.time

    def setNumber(self, number):
        self.number = number

    def setCourse(self, course):
        self.course = course

    def setType(self, type):
        self.type = type

    def setTime(self, time):
        self.time = time
