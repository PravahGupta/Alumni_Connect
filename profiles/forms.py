from django import forms
from .models import Profile, StatusChangeRequest, Skill
from batch.models import Batches


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'graduation_year', 'batch', 'current_role', 'company', 'linkedin_url', 'github_url', 'skills', 'bio', 'open_to_mentor', 'open_to_referral']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'graduation_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'batch': forms.Select(attrs={'class': 'form-control'}),
            'current_role' : forms.TextInput(attrs={'class': 'form-control'}),
            'company' : forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control'}),
            'skills': forms.CheckboxSelectMultiple(),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'open_to_mentor': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'open_to_referral': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class StatusChangeRequestForm(forms.ModelForm):
    class Meta:
        model = StatusChangeRequest
        fields = ['requested_user_type', 'reason']
        widgets = {
            'requested_user_type': forms.Select(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control'}),
        }