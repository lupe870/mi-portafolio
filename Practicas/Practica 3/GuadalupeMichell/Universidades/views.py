from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'universidad/index.html')

def alumnos(request):
    #datos = Alumno.objects.all()
    datos = {}
    return render(request, 'universidad/alumnos.html', {'alumnos': datos})

def carreras(request):
    #datos = Carrera.objects.all()
    datos = {}
    return render(request, 'universidad/carreras.html', {'carreras': datos})