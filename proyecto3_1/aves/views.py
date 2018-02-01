from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse,JsonResponse
from aves.models import *



# Create your views here.

def index(request):
    autores_count= Autor.objects.all().count()
    avistamiento= Avistamiento.objects.all().count()
    especie= Especie.objects.all().count
    count=[]


    #autores
    autores = []
    cantidades = []
    at = Autor.objects.all()
    avist = Avistamiento.objects.all()
    total = Avistamiento.objects.all().count()

    for a in at:
        cant = Avistamiento.objects.filter(id_autor=a.id_autor).count()
        autores.append([a.nombre_autor, cant])
        cantidades.append(cant)

    c1 = max(cantidades)
    cantidades.remove(c1)
    c2 = max(cantidades)
    cantidades.remove(c2)
    c3 = max(cantidades)
    valores = [c1, c2, c3]
    print
    valores
    for c in autores:
        if c[1] == c1:
            autor1 = c
            autor1[1] = autor1[1] * 100 / total
        if c[1] == c2:
            autor2 = c
            autor2[1] = autor2[1] * 100 / total
        if c[1] == c3:
            autor3 = c
            autor3[1] = autor3[1] * 100 / total


    autores = {'valores': valores, 'autor1': autor1, 'autor2': autor2, 'autor3': autor3, 'totalav': total,'autores':autores_count,'avistamiento': avistamiento,'especies':especie,'ubicaciones':avist }


    return render(request, 'index.html',autores)

def about(request):
    return render(request, 'about.html')

def autores(request):
    return render(request, 'autores.html')

def anios(request):
    return render(request, 'anios.html')
def aves(request):

    ubicaciones = Avistamiento.objects.all()


    return render(request, 'Aves.html',{'ubicaciones':ubicaciones })
def galeria(request):

    obj = Foto.objects.all().distinct('especie_id')

    paginator= Paginator(obj, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'galeria.html',{'contacts': contacts})




def uicn(request):
    return render(request, 'uicn.html')
def datoespecie(request,  id):
	j = Foto.objects.filter(especie = id)

	return render(request, 'datoespecie.html', {'img': j})





