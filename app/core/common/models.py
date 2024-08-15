from django.db import models
from app.core.base.models import BaseModel
from simple_history.models import HistoricalRecords
# Create your models here.

class Ubicacion(BaseModel):
    padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='hijos')
    descripcion = models.CharField('Ubicacion',max_length=255)
    nivel = models.PositiveIntegerField()
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Ubicacion'
        verbose_name_plural = 'Ubicaciones'
        db_table = 'Ubicaciones'
        ordering = ['id']

    def __str__(self):
        return f'{self.descripcion}'
    

    def desactivar(self):
        self.state = False
        self.save()

class TipoIdentificacion(BaseModel):
    detalle = models.CharField(max_length=20, unique=True) 
    historical = HistoricalRecords()
    
    class Meta:
        verbose_name = 'Tipo identificacion'
        verbose_name_plural = 'Tipos identificacion'
        db_table = 'Tipos_Identificacion'
        ordering = ['id']

    def __str__(self):
        return f'{self.detalle}'
    

    def desactivar(self):
        self.state = False
        self.save()

class Persona(BaseModel):
    tipo_identificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE, null=True, blank=True, related_name='Tipo_identificacion')
    numero_identificacion = models.CharField(max_length=20, unique=True)  # Campo único para la cédula
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