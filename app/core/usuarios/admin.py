from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.
@admin.register(Usuario)
class Usuario_Admin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    #search_fields = ('nombre')
    #list_filter = ('nombre')

# admin.site.unregister(Group)