from django.contrib import admin
from app.core.creditos.models import *
# Register your models here.

@admin.register(FormaPago)
class FormaPago_Admin(admin.ModelAdmin):
    list_display = ('id','descripcion')

@admin.register(TipoGarantia)
class TipoGarantia_Admin(admin.ModelAdmin):
    list_display = ('id','descripcion')

@admin.register(TipoSolicitud)
class TipoSolicitud_Admin(admin.ModelAdmin):
    list_display = ('id','descripcion')
    
@admin.register(TipoSegmentacion)
class TipoSegmentacion_Admin(admin.ModelAdmin):
    list_display = ('id','descripcion')

@admin.register(DetalleSolicitud)
class DetalleSolicitud_Admin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(SolicitudCredito)
class Solicitud_Admin(admin.ModelAdmin):
    list_display = ('id',)
