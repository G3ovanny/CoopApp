# Generated by Django 4.2 on 2024-06-15 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalusuario',
            old_name='tipoUsuario',
            new_name='tipo_suario',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='tipoUsuario',
            new_name='tipo_suario',
        ),
    ]
