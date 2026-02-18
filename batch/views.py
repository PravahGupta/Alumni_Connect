from django.shortcuts import render
from django.db.models import Count
from .models import Batches
from profiles.models import Profile

# Create your views here.
def batch_list(request, batch_id=None):
    if batch_id is None:
        batch = request.user.profile.batch
    else:
        batch = Batches.objects.get(id=batch_id)

    students = batch.profiles.select_related("user")

    return render(request, "batch/batch_list.html", {
        "batch": batch,
        "students": students
    })
