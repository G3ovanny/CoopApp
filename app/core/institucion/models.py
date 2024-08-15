from django.db import models
from simple_history.models import HistoricalRecords
from app.core.base.models import BaseModel

# Create your models here.


class Empresa(BaseModel):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    ruc = models.CharField(max_length=13, unique=True)
    email = models.EmailField(blank=True, null=True)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        db_table = 'Empresas'
        ordering = ['id']

    def __str__(self):
        return f'{self.id}'
    

    def desactivar(self):
        self.state = False
        self.save()

class Oficina(models.Model):
    empresa = models.ForeignKey(Empresa, related_name='oficinas', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'
        db_table = 'Oficinas'
        ordering = ['id']

    def __str__(self):
        return f'{self.id}'
    

    def desactivar(self):
        self.state = False
        self.save()
    