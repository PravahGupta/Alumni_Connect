# from django.shortcuts import render, get_object_or_404
# from accounts.models import Registrations
# from django.contrib.auth.decorators import login_required

# @login_required
# def profile_view(request, user_id):
#     user_obj = get_object_or_404(Registrations, id=user_id)
#     return render(request, 'profiles/profiles.html', {'profile_user': user_obj})

from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import Registrations
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def update_profile(request, user_id=None):
    if user_id is None:
        user_id = request.user.id

    user_obj = get_object_or_404(Registrations, id=user_id)
    profile_obj, created = Profile.objects.get_or_create(user=user_obj)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile_obj)
        if form.is_valid():
            form.save()
            return redirect('profile', user_id=user_obj.id)
    else:
        form = ProfileForm(instance=profile_obj)

    return render(request, 'profiles/update_profiles.html', {
        'profile_user': user_obj,
        'form': form
    })

@login_required
def profile_view(request, user_id=None):
    if user_id is None:
        user_id = request.user.id
    
    user_obj = get_object_or_404(Registrations, id=user_id)
    profile_obj, created = Profile.objects.get_or_create(user=user_obj)

    return render(request, 'profiles/profiles.html', {'profile_user': user_obj })
