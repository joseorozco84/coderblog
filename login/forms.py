from django import forms
from django.contrib.auth.forms import UserCreationForm
from login.models import User

class RegistrationForm(UserCreationForm):
    username = forms.TextInput()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
