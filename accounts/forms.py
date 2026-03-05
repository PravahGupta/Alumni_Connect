from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Registrations, MentorshipRequest

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        # db_table = ''
        # managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'
        model = Registrations
        fields = ['username', 'email', 'password1', 'password2']

class MentorshipForm(forms.ModelForm):
    class Meta:
        # db_table = ''
        # managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'
        model = MentorshipRequest
        fields = ['message', 'subject']
        widget = {
            'subject' : forms.TextInput(attrs={'class': 'form-control'}),
            'message' : forms.TextInput(attrs={'class': 'form-control'}),
        }