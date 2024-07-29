from django.db import models
from app.core.base.models import BaseModel
from simple_history.models import HistoricalRecords
from app.core.common.models import *
# Create your models here.

class FormaPago(BaseModel):
    descripcion = models.CharField('Descripcion', max_length=255)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'formas de pago'
        verbose_name_plural = 'formas de pago'
        db_table = 'Formas_Pago'
        ordering = ['id']

    def __str__(self):
        return f'{self.descripcion}'
    

    def desactivar(self):
        self.state = False
        self.save()


class TipoGarantia(BaseModel):
    descripcion = models.CharField('Descripcion', max_length=255)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Tipo de garantia'
        verbose_name_plural = 'Tipos de garantia'
        db_table = 'Tipo_Garantia'
        ordering = ['id']

    def __str__(self):
        return f'{self.descripcion}'
    

    def desactivar(self):
        self.state = False
        self.save()

class TipoSolicitud(BaseModel):
    descripcion = models.CharField('Descripcion', max_length=255)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Tipo de solicitud'
        verbose_name_plural = 'Tipos de solicitud'
        db_table = 'Tipo_Solicitud'
        ordering = ['id']

    def __str__(self):
        return f'{self.descripcion}'
    

    def desactivar(self):
        self.state = False
        self.save()

class TipoSegmentacion(BaseModel):
    descripcion = models.CharField('Descripcion', max_length=255)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Tipo de segmentacion'
        verbose_name_plural = 'Tipos de segmentacion'
        db_table = 'Tipo_Segmentacion'
        ordering = ['id']

    def __str__(self):
        return f'{self.descripcion}'
    

    def desactivar(self):
        self.state = False
        self.save()

class Solicitud(BaseModel):
    forma_pago = models.ForeignKey(FormaPago, on_delete=models.CASCADE, null=True, blank=True, related_name='FormaPago')
    tipo_garantia = models.ForeignKey(TipoGarantia, on_delete=models.CASCADE, null=True, blank=True, related_name='TipoGarantia')
    tipo_solicitud = models.ForeignKey(TipoSolicitud, on_delete=models.CASCADE, null=True, blank=True, related_name='TipoSolicitud')
    tipo_segmentacion = models.ForeignKey(TipoSegmentacion, on_delete=models.CASCADE, null=True, blank=True, related_name='TipoSegmentacion')
    lugar_solicitud = models.ForeignKey(EntidadAdministrativa, on_delete=models.CASCADE)
    fecha_solicitud  = models.DateField('Fecha de solicitud', auto_now=False, auto_now_add=False)
    taza_interes = models.DecimalField('Taza de interes', max_digits=5, decimal_places=2)
    monto = models.DecimalField('Monto', max_digits=5, decimal_places=2)
    plazo = models.IntegerField('Plazo')
    cuota = models.CharField('Cuota',null=True, blank=True, max_length=50)
    destino_credito = models.CharField('Destino del credito', null=True, blank=True, max_length=50)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        db_table = 'Solicitudes'
        ordering = ['id']

    def __str__(self):
        return f'{self.id}'
    

    def desactivar(self):
        self.state = False
        self.save()
        
class DetalleSolicitud(BaseModel):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, null=True, blank=True, related_name='Solicitud')
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Detalle de solicitud'
        verbose_name_plural = 'Detalles de solicitud'
        db_table = 'Detalles_Solicitud'
        ordering = ['id']

    def __str__(self):
        return f'{self.id}'
    

    def desactivar(self):
        self.state = False
        self.save()
