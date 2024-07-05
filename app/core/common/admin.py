from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(EntidadAdministrativa)
class EntidadAdministrativa_Admin(admin.ModelAdmin):
    list_display = ('id', 'padre', 'descripcion')

@admin.register(Persona)
class Persona_Admin(admin.ModelAdmin):
    list_display = ('id','cedula','apellido_paterno','apellido_materno','primer_nombre','segundo_nombre','fecha_nacimiento', 'state')