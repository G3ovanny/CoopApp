# Generated by Django 4.2 on 2024-06-15 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_rename_tipousuario_historicalusuario_tipo_suario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalusuario',
            old_name='tipo_suario',
            new_name='tipo_usuario',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='tipo_suario',
            new_name='tipo_usuario',
        ),
    ]
