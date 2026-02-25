from django.conf import settings
from django.db import models
from batch.models import Batches
from datetime import datetime

USER_TYPE_CHOICES = (
    ('student', 'Student'),
    ('alumni', 'Alumni'),
)

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=150, blank=True)
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='student'
    )
    graduation_year = models.IntegerField(null=True, blank=True)
    batch = models.ForeignKey(Batches, related_name="profiles", on_delete=models.SET_NULL, 
            null=True, blank=True)
    course = models.CharField(max_length=50, blank=True)  # moved from old Registrations
    current_role = models.CharField(max_length=150, blank=True)
    company = models.CharField(max_length=150, blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    bio = models.TextField(blank=True)
    open_to_mentor = models.BooleanField(default=False)
    open_to_referral = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
    
    def save(self, *args, **kwargs):
        current_year = datetime.now().year
        if self.graduation_year and self.graduation_year < current_year:
            self.user_type = 'alumni'
        else:
            self.user_type = 'student'
        super().save(*args, **kwargs)


class BatchAdmin(models.Model):
    is_batch_admin = models.BooleanField(default=False)

class StatusChangeRequest(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    requested_user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    reason = models.TextField()
    is_approved = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
