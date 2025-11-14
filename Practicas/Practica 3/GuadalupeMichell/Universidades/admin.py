from django.contrib import admin
from .models import *

# Register your models here.
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('nombrefacultad', 'cod_facultad', 'ubicación', 'is_active', 'foto')
    search_fields = ('nombrefacultad', 'cod_facultad')
    list_filter = ('is_active',)
    ordering = ('nombrefacultad',)

admin.site.register(Faculty, FacultyAdmin)

class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombrecarrera', 'cod_facultad', 'duracion_años', 'is_active', 'faculty')
    search_fields = ('nombrecarrera', 'cod_facultad')
    autocomplete_fields = ('faculty',)
    list_filter = ('is_active', 'faculty')
    ordering = ('nombrecarrera',)

admin.site.register(Carrera, CarreraAdmin)