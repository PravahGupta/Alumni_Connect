from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UniversityForm, InstitutionForm, ProgramForm
from .models import Program
from batch.models import Batches
from profiles.models import Skill

@login_required
def create_university(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UniversityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminpanel')
    else:
        form = UniversityForm()

    return render(request, 'institute/universitycreation.html', {'form': form})

@login_required
def create_institution(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    if request.method == 'POST':
        form = InstitutionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminpanel')
    else:
        form = InstitutionForm()

    return render(request, 'institute/institutecreation.html', {'form': form})

@login_required
def create_program(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminpanel')
    else:
        form = ProgramForm()

    return render(request, 'institute/programcreation.html', {'form': form})

@login_required
def create_skill(request):

    if not request.user.is_staff:
        return redirect('dashboard')

    if request.method == "POST":
        name = request.POST.get('name')

        if name:
            Skill.objects.create(name=name)
            return redirect('adminpanel')

    return render(request, 'institute/skillcreation.html')

@login_required
def create_batch(request):
    if not request.user.is_staff:
        return redirect('dashboard')
    programs = Program.objects.all()

    if request.method == "POST":
        program_id = request.POST.get('program_name')
        batch_name = request.POST.get('batch_name')
        start_year = request.POST.get('start_year')
        end_year = request.POST.get('end_year')
        program = Program.objects.get(id=program_id)

        Batches.objects.create(
            program_name=program,
            batch_name=batch_name,
            start_year=start_year,
            end_year=end_year
        )
        return redirect('adminpanel')

    return render(request, 'institute/batchcreation.html', {
        'programs': programs
    })
