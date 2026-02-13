from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Registrations
from .models import Profile


@receiver(post_save, sender=Registrations)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)