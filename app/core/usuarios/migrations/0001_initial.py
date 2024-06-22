# Generated by Django 4.2 on 2024-06-15 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='username')),
                ('clave_temporal', models.BooleanField(default=True)),
                ('fecha_clave', models.DateField(auto_now=True, null=True, verbose_name='Fecha cambio contraseña')),
                ('password', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='password')),
                ('correo', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Correo electrónico')),
                ('nombre', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre Usuario')),
                ('apellido_paterno', models.CharField(blank=True, max_length=255, null=True, verbose_name='Apellido Paterno')),
                ('tipoUsuario', models.IntegerField(blank=True, null=True, verbose_name='Tipo de usuario')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
                'db_table': 'Usuarios',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalUsuario',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(blank=True, db_index=True, max_length=30, null=True, verbose_name='username')),
                ('clave_temporal', models.BooleanField(default=True)),
                ('fecha_clave', models.DateField(blank=True, editable=False, null=True, verbose_name='Fecha cambio contraseña')),
                ('password', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='password')),
                ('correo', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Correo electrónico')),
                ('nombre', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre Usuario')),
                ('apellido_paterno', models.CharField(blank=True, max_length=255, null=True, verbose_name='Apellido Paterno')),
                ('tipoUsuario', models.IntegerField(blank=True, null=True, verbose_name='Tipo de usuario')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical usuario',
                'verbose_name_plural': 'historical usuarios',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
