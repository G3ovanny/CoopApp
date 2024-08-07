# Generated by Django 4.2 on 2024-07-08 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('creditos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalDetalleSolicitud',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de eliminación')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('solicitud', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='creditos.solicitud')),
            ],
            options={
                'verbose_name': 'historical Detalle de solicitud',
                'verbose_name_plural': 'historical Detalles de solicitud',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='DetalleSolicitud',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de eliminación')),
                ('solicitud', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Solicitud', to='creditos.solicitud')),
            ],
            options={
                'verbose_name': 'Detalle de solicitud',
                'verbose_name_plural': 'Detalles de solicitud',
                'db_table': 'Detalles_Solicitud',
                'ordering': ['id'],
            },
        ),
    ]
