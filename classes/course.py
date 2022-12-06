from Scheduler.models import Course, User
from user import User

class Course:
    def __init__(self, number, name, description, instructor, semester, year):
        self.number = number
        self.name = name
        self.description = description
        self.instructor = instructor
        self.semester = semester
        self.year = year

    def save(self):
        Course.objects.create(
            number=self.number,
            name=self.name,
            description=self.description,
            instructor=self.instructor,
            semester=self.semester,
            year=self.year,
        )
        return f"Course {self.number} created successfully"

    def getNumber(self):
        return self.number

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getInstructor(self):
        return self.instructor

    def getSemester(self):
        return self.semester

    def getYear(self):
        return self.year

    def setNumber(self, number):
        self.number = number

    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description

    def setInstructor(self, instructor):
        self.instructor = instructor

    def setSemester(self, semester):
        self.semester = semester

    def setYear(self, year):
        self.year = year
