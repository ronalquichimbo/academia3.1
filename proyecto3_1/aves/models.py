# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre_autor = models.TextField(blank=True, null=True)
    bibliografia = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autor'
    def __unicode__(self):
        return "%s - %s -%s" % (self.id_autor, self.nombre_autor, self.bibliografia)


class Avistamiento(models.Model):
    id_avistamiento = models.AutoField(primary_key=True)
    id_especie = models.ForeignKey('Especie', db_column='id_especie', blank=True, null=True)
    id_ubicacion = models.ForeignKey('Ubicacion', db_column='id_ubicacion', blank=True, null=True)
    anio_recoleccion = models.TextField(blank=True, null=True)
    anio_publicacion = models.TextField(blank=True, null=True)
    ecosistema = models.CharField(max_length=50, blank=True, null=True)
    comportamiento = models.NullBooleanField()
    llamado = models.NullBooleanField()
    ecologia = models.NullBooleanField()
    id_autor = models.ForeignKey(Autor, db_column='id_autor', blank=True, null=True)
    tipo_recurso = models.CharField(max_length=30, blank=True, null=True)
    morfometria = models.NullBooleanField()
    localidad = models.TextField(blank=True, null=True)
    altitud = models.IntegerField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    min_altitud = models.IntegerField(blank=True, null=True)
    max_altitud = models.IntegerField(blank=True, null=True)
    sitio = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avistamiento'
    def __unicode__(self):
        return "%s - %s -%s -%s -%s -%s -% s-%s -%s -%s -%s -%s -%s -%s -%s -%s -%s -%s -%s" % (self.id_avistamiento, self.id_especie, self.id_ubicacion,self.anio_recoleccion,self.anio_publicacion,self.ecosistema,self.comportamiento,self.llamado,self.ecologia,self.id_autor, self.tipo_recurso, self.morfometria,self.localidad,self.altitud,self.latitud,self.longitud,self.min_altitud,self.max_altitud,self.sitio)


class Especie(models.Model):
    id_especie = models.AutoField(primary_key=True)
    codigo_especie = models.CharField(unique=True, max_length=15, blank=True, null=True)
    familia = models.ForeignKey('Familia', db_column='familia', blank=True, null=True)
    especie = models.CharField(max_length=30, blank=True, null=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    sinonimo = models.CharField(max_length=30, blank=True, null=True)
    uicn = models.ForeignKey('Uicn', db_column='uicn', blank=True, null=True)
    endemismo = models.CharField(max_length=10, blank=True, null=True)
    migracion = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especie'
    def __unicode__(self):
        return "%s - %s -%s -%s -%s -%s -%s -%s -%s " % (self.id_especie, self.codigo_especie, self.familia,self.especie,self.nombre,self.sinonimo,self.uicn,self.endemismo,self.migracion)


class Familia(models.Model):
    id_familia = models.AutoField(primary_key=True)
    nombre_fam = models.CharField(max_length=50, blank=True, null=True)
    dependencia_fam = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'familia'
    def __unicode__(self):
        return "%s - %s -%s" % (self.id_familia, self.nombre_fam, self.dependencia_fam)


class Foto(models.Model):
    id_foto = models.AutoField(primary_key=True)
    especie = models.ForeignKey(Especie, db_column='especie', blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foto'
    def __unicode__(self):
        return "%s - %s -%s" % (self.id_foto, self.especie, self.url)

class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    nombre_ub = models.CharField(max_length=50, blank=True, null=True)
    dependencia_ub = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ubicacion'
    def __unicode__(self):
        return "%s - %s -%s" % (self.id_ubicacion, self.nombre_ub, self.dependencia_ub)


class Uicn(models.Model):
    id_uicn = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=10, blank=True, null=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uicn'
    def __unicode__(self):
        return "%s - %s -%s" % (self.id_uicn, self.estado, self.descripcion)
