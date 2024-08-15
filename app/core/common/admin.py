from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Ubicacion)
class Ubicacion_Admin(admin.ModelAdmin):
    list_display = ('id', 'padre', 'descripcion', 'nivel')

@admin.register(Persona)
class Persona_Admin(admin.ModelAdmin):
    list_display = ('id', 'numero_identificacion','apellido_paterno','apellido_materno','primer_nombre','segundo_nombre','fecha_nacimiento', 'state')