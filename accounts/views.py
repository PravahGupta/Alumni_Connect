from urllib import response
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Registrations, MentorshipRequest
from .forms import RegistrationForm, MentorshipForm
from profiles.models import Profile

# Create your views here.
def index(request):
    return render(request, 'accounts/landing.html')

@login_required
def dashboard(request):
    # session_data = request.session.items()
    # Or print them to your server console for debugging
    # for key, value in request.session.items():
    #     print(f"{key} => {value}")

    # print("--- REQUEST META ---")
    # for key, value in request.META.items():
    #     print(f"{key}: {value}")

    # # 2. Print User Details (provided by AuthenticationMiddleware)
    # print(f"User: {request.user} (Authenticated: {request.user.is_authenticated})")

    # # 3. Print basic Request attributes
    # print(f"Path: {request.path}")
    # print(f"Method: {request.method}")
    # print(f"Scheme: {request.scheme}")
    
    return render(request, 'accounts/dashboard.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('verify')

        user = Registrations.objects.filter(
            name=username,
            password=password
        ).first()
        if user:
            request.session['user_id'] = user.id
            response = redirect('dashboard')
            try:
                response.set_cookie(
                key='user_id',
                value=user.id,
                httponly=True,
                secure=True,
                samesite='Lax'
                )
            except Registrations.DoesNotExist:
                pass
            return response

        else:
            messages.error(request, "Username or Password does not match.")
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})

@login_required
def mentorshipRequest(request, receiver):
    mentor = get_object_or_404(Profile, pk=receiver)

    if request.method == 'POST' and mentor.open_to_mentor:
        form = MentorshipForm(request.POST)
        
        if form.is_valid():
            if MentorshipRequest.objects.filter(sender=request.user,receiver=mentor).exists():
                messages.error(request, "!! You have already sent a request to this mentor !!")
            else:
                mentorship = form.save(commit=False)
                mentorship.sender = request.user
                mentorship.receiver = mentor
                mentorship.save()
                messages.success(request, "!! The Mentorship Request is Successfully Sent !!")
            return redirect('dashboard')
    else:
        form = MentorshipForm()
    return render(request, 'profiles/requestMentor.html', {'form' : form, 'mentor': mentor})

@login_required
def viewConnections(request):
    connect = MentorshipRequest.objects.filter(status_choice='accepted')
    print(connect)
    return render(request, 'batch/connections.html', {'connect': connect})

@login_required
def adminpanel(request):
    if request.user.username == 'Pravah':
        return render(request, 'accounts/adminindex.html')
    else:
        return redirect('dashboard')