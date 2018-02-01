from django.contrib import admin

from aves.models import *

class AutorAdmin(admin.ModelAdmin):
    list_display = ('id_autor','nombre_autor', 'bibliografia')

class AvistamientoAdmin(admin.ModelAdmin):
    list_display = ('id_avistamiento','id_especie', 'id_ubicacion','anio_recoleccion','anio_publicacion','ecosistema','comportamiento','llamado','ecologia','id_autor','tipo_recurso','morfometria','localidad','altitud','latitud','longitud','min_altitud','max_altitud','sitio')

class EspecieAdmin(admin.ModelAdmin):
    list_display = ('id_especie','codigo_especie', 'familia','especie','nombre','sinonimo','uicn','endemismo','migracion')

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('id_familia','nombre_fam', 'dependencia_fam')

class FotoAdmin(admin.ModelAdmin):
    list_display = ('id_foto','especie', 'url')

class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('id_ubicacion','nombre_ub', 'dependencia_ub')

class UicAdmin(admin.ModelAdmin):
    list_display = ('id_uicn','estado', 'descripcion')

admin.site.register(Autor,AutorAdmin)
admin.site.register(Avistamiento,AvistamientoAdmin)
admin.site.register(Especie,EspecieAdmin)
admin.site.register(Familia, FamiliaAdmin)
admin.site.register(Foto,FotoAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)
admin.site.register(Uicn,UicAdmin)
