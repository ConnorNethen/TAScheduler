from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import AppUser


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('pID', 'email', 'address', 'phone',)


class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = AppUser
        fields = ('pID', 'email', 'address', 'phone',)
