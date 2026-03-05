from django.contrib import admin
from .models import University, Institution, Program

# Register your models here.
@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'institute_name', 'university')
    search_fields = ('institute_name',)
    list_filter = ('university',)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'degree_level', 'institute', 'allowed_strength')
    search_fields = ('name', 'degree_level')
    list_filter = ('degree_level', 'institute')
