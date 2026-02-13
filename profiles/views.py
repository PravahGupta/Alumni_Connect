from django.shortcuts import render, get_object_or_404
from accounts.models import Registrations

# Create your views here.

def profile_view(request, user_id):
    user = get_object_or_404(Registrations, id=user_id)
    profile = user.profile

    return render(request, "profile.html", {
        "user": user,
        "profile": profile
    })
