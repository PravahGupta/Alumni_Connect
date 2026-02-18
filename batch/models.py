from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Batches(models.Model):
    batch_name = models.CharField()
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.batch_name
