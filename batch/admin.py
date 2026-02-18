from django.contrib import admin
from .models import Batches

# Register your models here.
@admin.register(Batches)
class AdminBatch(admin.ModelAdmin):
    list_display = ('id', 'batch_name', 'start_year', 'end_year')

    