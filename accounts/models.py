from django.db import models

# Create your models here.
class Registrations(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField()
    course = models.CharField(max_length=50)
    batch = models.CharField()
    otp = models.IntegerField(null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name