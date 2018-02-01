from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'about$',views.about,name='about'),
    url(r'autores$',views.autores,name='autores'),
    url(r'anios$',views.anios,name='anios'),
    url(r'aves$',views.aves,name='aves'),
    url(r'galeria$',views.galeria,name='galeria'),
    url(r'uicn$',views.uicn,name='uicn'),
    url(r'especie/(?P<id>\d+)$',views.datoespecie,name='datoespecie'),


]
