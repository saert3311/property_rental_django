# Generated by Django 5.0.6 on 2024-05-13 21:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_provincia_regiones_comuna_provincia_cod_region'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('m2_building', models.IntegerField(verbose_name='Metros cuadrados construidos')),
                ('m2_total', models.IntegerField(verbose_name='Metros cuadrados totales')),
                ('n_parking', models.IntegerField(verbose_name='Número de estacionamientos')),
                ('n_bedrooms', models.IntegerField(verbose_name='Número de dormitorios')),
                ('n_bathrooms', models.IntegerField(verbose_name='Número de baños')),
                ('address', models.CharField(max_length=200, verbose_name='Dirección')),
                ('ptype', models.SmallIntegerField(choices=[(0, 'Casa'), (1, 'Departamento'), (2, 'Parcela'), (3, 'Local')], default=0, verbose_name='Tipo')),
                ('price', models.IntegerField(verbose_name='Precio')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.comuna', verbose_name='Comuna')),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Arrendador')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('origin_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userdata')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('origin_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.request')),
            ],
        ),
    ]
