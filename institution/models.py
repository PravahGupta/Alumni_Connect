from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Institution(models.Model):
    institute_name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='institutions')

    def __str__(self):
        return f"{self.institute_name} ({self.university.name})"

class Program(models.Model):
    institute = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='programs')
    name = models.CharField(max_length=100)
    degree_level = models.CharField(max_length=50)
    allowed_strength = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.name} - {self.degree_level} ({self.institute.institute_name})"
