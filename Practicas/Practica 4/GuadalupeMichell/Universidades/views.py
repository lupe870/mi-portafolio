from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

@login_required
def index(request):
    return render(request, 'universidad/index.html')

@login_required
def alumnos(request):
    alumnos = Estudiante.objects.filter(is_active=True)
    return render(request, 'universidad/alumnos.html', {'alumnos': alumnos})

@login_required
def carreras(request):
    carreras = Carrera.objects.filter(is_active=True)
    return render(request, 'universidad/carreras.html', {'carreras': carreras})