from django.db import models
from accounts.models import Registrations

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(Registrations, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=150, blank=True)
    user_type = models.CharField(max_length=50, blank=True)
    graduation_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.email
