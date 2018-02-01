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

#inicio vista autores
def autores(request):

    autores=[]
    cantidades=[]
    top=[]
    at=Autor.objects.all()
    avist=Avistamiento.objects.all()
    total=Avistamiento.objects.all().count()

    for a in at:
        cant=Avistamiento.objects.filter(id_autor=a.id_autor).count()
        if(cant>500):
            top.append([a.nombre_autor,cant])
        
        autores.append([a.nombre_autor,cant])
        cantidades.append(cant)

    autores= {'autores':autores,'top':top, 'totalav':total}
    return render(request, 'autores.html',autores,
        context_instance = RequestContext(request))
#fin vista autores

def anios(request):
    avistamientos = Avistamiento.objects.all()
    lista=[]
    for a in avistamientos:
        lista.append(a.anio_recoleccion)
    
    listaA=list(set(lista))
    avist=[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    for l in listaA:
        cant= Avistamiento.objects.filter(anio_recoleccion=l).count()
        av_e= Avistamiento.objects.filter(anio_recoleccion=l)
        es=[]
        for e in av_e:
            es.append(e.id_especie)

        es=list(set(es))
        if l=='null':
            nulos=[str(l), cant, len(es)]
        else:
            avist.append([str(l), cant, len(es)])
        

    anios= {'avistamientos':avist}
    return render(request, 'anios.html',anios,
        context_instance = RequestContext(request))

#incio aves
def aves(request):

    ubicaciones = Avistamiento.objects.all()
    #Provincias y avistamientos
    provincias=[]
    paises=[]
    pr=Ubicacion.objects.all()
    for p in pr:
        cant=Avistamiento.objects.filter(id_ubicacion=p.id_ubicacion).count()
        provincias.append([p.id_ubicacion,p.nombre_ub,p.dependencia_ub,cant])

    paises.append(provincias[0])
    del provincias[0]#elimino la primera posicion del arreglo Ecuador y lo agrego al la lista paises
    paises.append(provincias[0])
    del provincias[0]#elimino la nueva primera posicion del arreglo Peru y lo agrego al la lista paises

    anios= {'provincias':provincias,'paises':paises,'ubicaciones':ubicaciones }

    return render(request, 'Aves.html',anios, context_instance=RequestContext(request))
#fin aves

# inicio vista galeria de aves
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
    uicn_esp=[]
    uicn=Uicn.objects.all()
    colores=["#0D8ECF","#0D52D1","#8A0CCF","#CD0D74","#754DEB","#DDDDDD","#999999"]
    i=0
    for u in uicn:
         esp=Especie.objects.filter(uicn=u.id_uicn).count()
         uicn_esp.append([u.estado,esp,colores[i]])
         i=i+1

    anios= {'uicn':uicn_esp}
    return render(request, 'uicn.html',anios,
        context_instance = RequestContext(request))
    
def datoespecie(request,  id):
	j = Foto.objects.filter(especie = id)

	return render(request, 'datoespecie.html', {'img': j})





