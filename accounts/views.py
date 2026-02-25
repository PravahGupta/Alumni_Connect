from urllib import response
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Registrations
from .forms import RegistrationForm

# Create your views here.
def index(request):
    return render(request, 'accounts/landing.html')

@login_required
def dashboard(request):
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