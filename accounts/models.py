from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Registrations(AbstractUser):
    otp = models.IntegerField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username