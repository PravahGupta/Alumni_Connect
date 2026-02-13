from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Registrations

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return HttpResponse("Login is coming your way soon! please wait")

def logout(request):
    pass

def registration(request):
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        course = request.POST.get('course')
        batch = request.POST.get('batch')
        register = Registrations(name=name, email=email, password=password, course=course, batch=batch)
        register.save()
        return redirect('login')

    return render(request, 'registration.html')