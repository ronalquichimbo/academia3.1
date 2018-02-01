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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre_autor = models.TextField(blank=True, null=True)
    bibliografia = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autor'


class Avistamiento(models.Model):
    id_avistamiento = models.AutoField(primary_key=True)
    id_especie = models.ForeignKey('Especie', db_column='id_especie', blank=True, null=True)
    id_ubicacion = models.ForeignKey('Ubicacion', db_column='id_ubicacion', blank=True, null=True)
    anio_recoleccion = models.TextField(blank=True, null=True)
    anio_publicacion = models.TextField(blank=True, null=True)
    ecosistema = models.CharField(max_length=150, blank=True, null=True)
    comportamiento = models.CharField(max_length=20, blank=True, null=True)
    llamado = models.CharField(max_length=20, blank=True, null=True)
    ecologia = models.CharField(max_length=20, blank=True, null=True)
    id_autor = models.ForeignKey(Autor, db_column='id_autor', blank=True, null=True)
    tipo_recurso = models.CharField(max_length=30, blank=True, null=True)
    morfometria = models.CharField(max_length=70, blank=True, null=True)
    localidad = models.TextField(blank=True, null=True)
    altitud = models.IntegerField(blank=True, null=True)
    latitud = models.CharField(max_length=50, blank=True, null=True)
    longitud = models.CharField(max_length=50, blank=True, null=True)
    min_altitud = models.IntegerField(blank=True, null=True)
    max_altitud = models.IntegerField(blank=True, null=True)
    sitio = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avistamiento'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Especie(models.Model):
    id_especie = models.AutoField(primary_key=True)
    codigo_especie = models.CharField(unique=True, max_length=15, blank=True, null=True)
    familia = models.ForeignKey('Familia', db_column='familia', blank=True, null=True)
    especie = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    sinonimo = models.TextField(blank=True, null=True)
    uicn = models.ForeignKey('Uicn', db_column='uicn', blank=True, null=True)
    endemismo = models.CharField(max_length=20, blank=True, null=True)
    migracion = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especie'


class Familia(models.Model):
    id_familia = models.AutoField(primary_key=True)
    nombre_fam = models.CharField(max_length=50, blank=True, null=True)
    dependencia_fam = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'familia'


class Foto(models.Model):
    id_foto = models.AutoField(primary_key=True)
    especie = models.ForeignKey(Especie, db_column='especie', blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foto'


class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    nombre_ub = models.CharField(max_length=50, blank=True, null=True)
    dependencia_ub = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ubicacion'


class Uicn(models.Model):
    id_uicn = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=10, blank=True, null=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uicn'
