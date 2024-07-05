from django.db import models
from app.core.base.models import BaseModel
from simple_history.models import HistoricalRecords
# Create your models here.

class EntidadAdministrativa(BaseModel):
    descripcion = models.CharField('Entidad Administrativa',max_length=255)
    padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='Entidad_Administrativa')
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'entidad_administrativa'
        verbose_name_plural = 'entidades_administrativas'
        db_table = 'Entidad_Administrativas'
        ordering = ['id','descripcion']

    def __str__(self):
        return f'{self.descripcion}'
    

    def desactivar(self):
        self.state = False
        self.save()


class Persona(BaseModel):
    cedula = models.CharField(max_length=20, unique=True)  # Campo único para la cédula
    apellido_paterno = models.CharField(max_length=50)  # Apellido paterno
    apellido_materno = models.CharField(max_length=50)  # Apellido materno
    primer_nombre = models.CharField(max_length=50)  # Primer nombre
    segundo_nombre = models.CharField(max_length=50)  # Segundo nombre
    fecha_nacimiento = models.DateField()  # Fecha de nacimiento
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'persona'
        verbose_name_plural = 'personas'
        db_table = 'Personas'
        ordering = ['apellido_paterno']

    def __str__(self):
        return f'{self.apellido_paterno}'
    

    def desactivar(self):
        self.state = False
        self.save()