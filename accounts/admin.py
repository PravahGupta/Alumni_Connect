from django.contrib import admin
from accounts.models import Registrations

# Register your models here.
@admin.register(Registrations)
class Register(admin.ModelAdmin):
    list_display = ("name", "email", "batch", "course")
    exclude = ('password',)