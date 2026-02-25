from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Registrations

@admin.register(Registrations)
class RegisterAdmin(UserAdmin):
    list_display = ['id', 'username', 'email', 'is_verified', 'is_staff']