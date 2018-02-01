from django.conf.urls import patterns, url

from aves import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # url(r'buscador$', views.buscador_placas, name='buscador_placas'),
    # url(r'buscador_2$', views.buscador_placas_dos, name='buscador_placas_dos'),
    # url(r'funcion_ajax/$', views.funcion_ajax, name='funcion_ajax'),
    # url(r'funcion_ajax_dos/$', views.funcion_ajax_dos, name='funcion_ajax_dos'),
    # url(r'provincia/(?P<id>\d+)/mivista/aplicacion$', views.provincia, name='provincia'),
)
