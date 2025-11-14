from django.db import models
from django.utils import timezone

# Create your models here.
class Estudiante(models.Model):
    nombreestudiante = models.CharField(max_length=100)
    cod_estudiante = models.CharField(max_length=20)
    email = models.CharField()
    is_active = models.BooleanField(default=True)
    fecha_inscriccion = models.DateField(default= timezone.now)
    Carrera = models.ForeignKey(
        'Carrera',
        on_delete= models.CASCADE,
        related_name= 'Estudiantes',
        null= True,
        blank= True
    )

    def __str__(self):
        return self.nombreestudiante
    
    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

class Materia(models.Model):
    nombremateria = models.CharField(max_length=100)
    cod_materia = models.CharField(max_length=20)
    nivel = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    Carrera = models.ForeignKey(
        'Carrera',
        on_delete= models.CASCADE,
        related_name= 'materias',
        null= True,
        blank= True
    )

    def __str__(self):
        return self.nombremateria
    
    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

class Programar_Materia(models.Model):
    student = models.ForeignKey(
        Estudiante,
        on_delete= models.CASCADE,
        related_name='programar_student',
        null=True,
        blank= True
    )
    subject = models.ForeignKey(
        Materia,
        on_delete= models.CASCADE,
        related_name= 'programar_subject',
        null=True,
        blank= True
    )

    is_active = models.BooleanField(default=True, verbose_name='¿Esta activa la programacion?')
    fecha_programación = models.DateField(default= timezone.now)

    class Meta:
        verbose_name = 'Programar materias'
        verbose_name_plural = 'Programar materias'
        unique_together = ('student', 'subject', 'fecha_programación')
        
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