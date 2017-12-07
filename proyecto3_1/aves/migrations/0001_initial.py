# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id_autor', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_autor', models.TextField(null=True, blank=True)),
                ('bibliografia', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'autor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Avistamiento',
            fields=[
                ('id_avistamiento', models.AutoField(serialize=False, primary_key=True)),
                ('anio_recoleccion', models.TextField(null=True, blank=True)),
                ('anio_publicacion', models.TextField(null=True, blank=True)),
                ('ecosistema', models.CharField(max_length=50, null=True, blank=True)),
                ('comportamiento', models.NullBooleanField()),
                ('llamado', models.NullBooleanField()),
                ('ecologia', models.NullBooleanField()),
                ('tipo_recurso', models.CharField(max_length=30, null=True, blank=True)),
                ('morfometria', models.NullBooleanField()),
                ('localidad', models.TextField(null=True, blank=True)),
                ('altitud', models.IntegerField(null=True, blank=True)),
                ('latitud', models.FloatField(null=True, blank=True)),
                ('longitud', models.FloatField(null=True, blank=True)),
                ('min_altitud', models.IntegerField(null=True, blank=True)),
                ('max_altitud', models.IntegerField(null=True, blank=True)),
                ('sitio', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'avistamiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id_especie', models.AutoField(serialize=False, primary_key=True)),
                ('codigo_especie', models.CharField(max_length=15, unique=True, null=True, blank=True)),
                ('especie', models.CharField(max_length=30, null=True, blank=True)),
                ('nombre', models.CharField(max_length=30, null=True, blank=True)),
                ('sinonimo', models.CharField(max_length=30, null=True, blank=True)),
                ('endemismo', models.CharField(max_length=10, null=True, blank=True)),
                ('migracion', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'db_table': 'especie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id_familia', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_fam', models.CharField(max_length=50, null=True, blank=True)),
                ('dependencia_fam', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'familia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id_foto', models.AutoField(serialize=False, primary_key=True)),
                ('url', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'foto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id_ubicacion', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_ub', models.CharField(max_length=50, null=True, blank=True)),
                ('dependencia_ub', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'ubicacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Uicn',
            fields=[
                ('id_uicn', models.AutoField(serialize=False, primary_key=True)),
                ('estado', models.CharField(max_length=10, null=True, blank=True)),
                ('descripcion', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
                'db_table': 'uicn',
                'managed': False,
            },
        ),
    ]
