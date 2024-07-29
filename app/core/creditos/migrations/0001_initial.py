# Generated by Django 4.2 on 2024-07-08 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de eliminación')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'formas de pago',
                'verbose_name_plural': 'formas de pago',
                'db_table': 'Formas_Pago',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TipoGarantia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de eliminación')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo de garantia',
                'verbose_name_plural': 'Tipos de garantia',
                'db_table': 'Tipo_Garantia',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TipoSegmentacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de eliminación')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo de segmentacion',
                'verbose_name_plural': 'Tipos de segmentacion',
                'db_table': 'Tipo_Segmentacion',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TipoSolicitud',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de eliminación')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo de solicitud',
                'verbose_name_plural': 'Tipos de solicitud',
                'db_table': 'Tipo_Solicitud',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de eliminación')),
                ('fecha_solicitud', models.DateField(verbose_name='Fecha de solicitud')),
                ('taza_interes', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Taza de interes')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Monto')),
                ('plazo', models.IntegerField(verbose_name='Plazo')),
                ('cuota', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cuota')),
                ('destino_credito', models.CharField(blank=True, max_length=50, null=True, verbose_name='Destino del credito')),
                ('forma_pago', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FormaPago', to='creditos.formapago')),
                ('lugar_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.entidadadministrativa')),
                ('tipo_garantia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TipoGarantia', to='creditos.tipogarantia')),
                ('tipo_segmentacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TipoSegmentacion', to='creditos.tiposegmentacion')),
                ('tipo_solicitud', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TipoSolicitud', to='creditos.tiposolicitud')),
            ],
            options={
                'verbose_name': 'Solicitud',
                'verbose_name_plural': 'Solicitudes',
                'db_table': 'Solicitudes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalTipoSolicitud',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de eliminación')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Tipo de solicitud',
                'verbose_name_plural': 'historical Tipos de solicitud',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTipoSegmentacion',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de eliminación')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Tipo de segmentacion',
                'verbose_name_plural': 'historical Tipos de segmentacion',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTipoGarantia',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de eliminación')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Tipo de garantia',
                'verbose_name_plural': 'historical Tipos de garantia',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSolicitud',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de eliminación')),
                ('fecha_solicitud', models.DateField(verbose_name='Fecha de solicitud')),
                ('taza_interes', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Taza de interes')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Monto')),
                ('plazo', models.IntegerField(verbose_name='Plazo')),
                ('cuota', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cuota')),
                ('destino_credito', models.CharField(blank=True, max_length=50, null=True, verbose_name='Destino del credito')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('forma_pago', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='creditos.formapago')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('lugar_solicitud', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='common.entidadadministrativa')),
                ('tipo_garantia', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='creditos.tipogarantia')),
                ('tipo_segmentacion', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='creditos.tiposegmentacion')),
                ('tipo_solicitud', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='creditos.tiposolicitud')),
            ],
            options={
                'verbose_name': 'historical Solicitud',
                'verbose_name_plural': 'historical Solicitudes',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFormaPago',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de eliminación')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical formas de pago',
                'verbose_name_plural': 'historical formas de pago',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
