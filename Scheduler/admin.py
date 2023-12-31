from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AppUserCreationForm, AppUserChangeForm
from .models import AppUser


class AppUserAdmin(UserAdmin):
    add_form = AppUserCreationForm
    form = AppUserChangeForm
    model = AppUser
    list_display = ('pID', 'email', 'is_staff', 'is_active',)
    list_filter = ('pID', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('pID', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('pID', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('pID', 'email',)
    ordering = ('pID', 'email',)


admin.site.register(AppUser, AppUserAdmin)
