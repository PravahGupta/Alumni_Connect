from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from profiles.models import Profile

# Create your models here.
class Registrations(AbstractUser):
    otp = models.IntegerField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
STATUS_TYPE_CHOICES = (
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('declined', 'Declined'),
)

class MentorshipRequest(models.Model):
    sender =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mentorRequest")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="mentorReq")
    pair_key = models.CharField(max_length=100, unique=True, editable=False, null=True)
    message = models.TextField(max_length=300)
    subject = models.CharField(max_length=50)
    status_choice = models.CharField(
        max_length=15,
        choices=STATUS_TYPE_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['sender', 'receiver'],
                name='unique_mentorship_request'
            )
        ]

    def save(self, *args, **kwargs):
        if self.sender == self.receiver.user:
            raise ValueError("Cannot send mentorship request to yourself.")
        
        # Normalize pair (smallest id first)
        low = min(self.sender_id, self.receiver_id)
        high = max(self.sender_id, self.receiver_id)
        self.pair_key = f"{low}_{high}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.receiver.full_name
