from django.db import models

# Create your models here.
class Carrera(models.Model):
    nombrecarrera = models.CharField(max_length=100)
    cod_facultad = models.CharField(max_length=20)
    duracion_años = models.IntegerField()
    is_active = models.BooleanField(default=True)
    faculty = models.ForeignKey(
        'Faculty',
        on_delete=models.CASCADE,
        related_name='Carreras',
        null= True,
        blank= True
    )

    def __str__(self):
        return self.nombrecarrera
    
    class Mete:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'

class Faculty(models.Model):
    nombrefacultad = models.CharField(max_length=100)
    cod_facultad = models.CharField(max_length=20)
    ubicación = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='Universidades/universidad/static/facultad_fotos/', null=True, blank= True)

    def __str__(self):
        return self.nombrefacultad
    
    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultades"