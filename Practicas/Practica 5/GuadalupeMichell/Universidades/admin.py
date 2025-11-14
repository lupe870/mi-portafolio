from django.contrib import admin
from .models import *

# Register your models here.
class CarreraInline(admin.TabularInline):
    model = Carrera
    extra = 1
    #autocomplete_fields = ('faculty',)

# Register your models here.
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('nombrefacultad', 'cod_facultad', 'ubicación', 'is_active', 'foto')
    search_fields = ('nombrefacultad', 'cod_facultad')
    list_filter = ('is_active',)
    ordering = ('nombrefacultad',)
    inlines = [CarreraInline]

admin.site.register(Faculty, FacultyAdmin)

class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombrecarrera', 'cod_facultad', 'duracion_años', 'is_active', 'faculty')
    search_fields = ('nombrecarrera', 'cod_facultad')
    autocomplete_fields = ('faculty',)
    list_filter = ('is_active', 'faculty')
    ordering = ('nombrecarrera',)

admin.site.register(Carrera, CarreraAdmin)

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombreestudiante', 'cod_estudiante', 'email', 'is_active', 'fecha_inscriccion', 'Carrera')
    search_fields = ('nombreestudiante', 'cod_estudiante')
    autocomplete_fields = ('Carrera', )
    list_filter = ('fecha_inscriccion', 'is_active')
    ordering = ('nombreestudiante',)

admin.site.register(Estudiante, EstudianteAdmin)

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombremateria', 'cod_materia', 'nivel', 'is_active')
    search_fields = ('nombremateria', 'cod_materia')
    list_filter = ('is_active', 'nivel', 'Carrera')

admin.site.register(Materia, MateriaAdmin)

class Programar_MateriaAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'is_active', 'fecha_programación')

admin.site.register(Programar_Materia, Programar_MateriaAdmin)