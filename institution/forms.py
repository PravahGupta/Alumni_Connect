from django import forms
from .models import University, Institution, Program

class UniversityForm(forms.ModelForm):
    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'
        model = University
        fields = ['name']

class InstitutionForm(forms.ModelForm):
    class Meta:
        verbose_name = 'Institute'
        verbose_name_plural = 'Institutes'
        model = Institution
        fields = ['institute_name', 'university']

class ProgramForm(forms.ModelForm):
    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'
        model = Program
        fields = ['institute', 'name', 'degree_level', 'allowed_strength']
