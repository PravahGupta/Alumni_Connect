from django import forms
from .models import Profile, StatusChangeRequest
from batch.models import Batches


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'graduation_year', 'batch']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_type': forms.TextInput(attrs={'class': 'form-control'}),
            'graduation_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'batch': forms.Select(attrs={'class': 'form-control'}),
        }

class StatusChangeRequestForm(forms.ModelForm):
    class Meta:
        model = StatusChangeRequest
        fields = ['requested_user_type', 'reason']
        widgets = {
            'requested_user_type': forms.Select(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control'}),
        }