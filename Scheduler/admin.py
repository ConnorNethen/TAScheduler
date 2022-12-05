from django.contrib import admin
from .models import Address, ContactInfo, Status, User, Course, Section, UserToSection

# Register your models here.
admin.site.register(Address)
admin.site.register(ContactInfo)
admin.site.register(Status)
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(UserToSection)