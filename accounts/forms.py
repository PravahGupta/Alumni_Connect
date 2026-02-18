from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Registrations

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Registrations
        fields = ['username', 'email', 'password1', 'password2']