from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

from aves.models import *


# Create your views here.
def index(request):
	#imagen ={'dir_imagen':"La Sazon de la Abuela"}
	img = Foto.objects.get(pk=72)
	imagen ={'dir_imagen':img}
	return render(request, 'index.html',imagen,
		context_instance = RequestContext(request))
