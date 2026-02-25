from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import Registrations
from .models import Profile, Skill
from batch.models import Batches
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator


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

@login_required
def search(request):
    print('got request')
    return render(request, 'batch/network.html')

@login_required
def see_profile(request): 
    try:
        username = request.GET.get("username")
        print(username)
        batch = request.GET.get("batch")
        user_obj = get_object_or_404(Registrations, username=username)
        print(user_obj, 'hello')
        profile_obj = get_object_or_404(Profile, id=user_obj.id)
        print(profile_obj)

        return render(request, 'profiles/profiles.html', {'profile_user': user_obj })
    except:
        print('There is a error')
        redirect('profile/')

@login_required
def alumni_dir(request):
    profiles = Profile.objects.select_related("user", "batch")\
                          .prefetch_related("skills")\
                          .exclude(user=request.user)
    query = request.GET.get("q")
    if query:
        profiles = profiles.filter(
            Q(user__fullname__icontains=query) |
            Q(user__username__icontains=query) |
            Q(company__icontains=query)
        )
    
    batch = request.GET.get("batch")
    skill = request.GET.get("skill")
    company = request.GET.get("company")
    mentor = request.GET.get("mentor")

    if batch:
        profiles = profiles.filter(batch_id=batch)

    if skill:
        profiles = profiles.filter(skills__id=skill)

    if company:
        profiles = profiles.filter(company__icontains=company)

    if mentor == "true":
        profiles = profiles.filter(open_to_mentor=True)
    
    paginator = Paginator(profiles, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    
    return render(request, "batch/directory.html", {
        "page_obj": page_obj,
        "batches": Batches.objects.all(),
        "skills": Skill.objects.all(),
    })

