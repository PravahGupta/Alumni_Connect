from django.contrib import admin
from .models import Profile, Skill

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "full_name", "user_type", "graduation_year", 'batch')
    search_fields = ("user__email", "full_name")

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)