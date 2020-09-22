from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class InvestigadoresView(ListView):
	model=Investigador
	template_name="app/investigadores_list.html"
	paginate_by = 24

class InvestigadorDetalleView(DetailView):
	model = Investigador

class PublicacionesView(ListView):
	model=Publicacion
	template_name="app/publicaciones_list.html"
	paginate_by = 24

def PublicacionesView(request, cat='nn'):
	if cat=='nn':
		publicaciones = Publicacion.objects.all()
	else:
		publicaciones = Publicacion.objects.filter(categoria=cat)
	contexto = {'publicaciones': publicaciones}
	return render (request, 'app/publicaciones_list.html', contexto)

class PublicacionDetalleView(DetailView):
	model = Publicacion

class ProyectosView(ListView):
	model=Proyecto
	template_name="app/proyectos_list.html"
	paginate_by = 24

class ProyectoDetalleView(DetailView):
	model = Proyecto

class ActividadesView(ListView):
	model=Actividad
	template_name="app/actividades_list.html"
	paginate_by = 24

class ActividadDetalleView(DetailView):
	model = Actividad

class NovedadesView(ListView):
	model=Novedad
	template_name="app/novedades_list.html"
	paginate_by = 24

	def get_context_data(self, **kwargs):
		context = super(NovedadesView, self).get_context_data(**kwargs)
		context['publicaciones'] = Publicacion.objects.filter(es_novedad=True)
		return context

def NovedadesView(request):
	template_name="app/novedades_list.html"
	novedades = Novedad.objects.all()
	publicaciones = Publicacion.objects.filter(es_novedad=True)
	context = {'publicaciones':publicaciones, 'novedades':novedades}
	return render(request, template_name, context)

class NovedadDetalleView(DetailView):
	model = Novedad

class DatosView(ListView):
	model=Dato
	template_name="app/datos_list.html"
	paginate_by = 24

class DatoDetalleView(DetailView):
	model = Dato

def PublicacionesIIEP(request):
	publicacion = PublicacionIIEP.objects.using('iiep').all().filter(categoria_id=3).order_by('-id')
	page = request.GET.get('page', 1)
	paginator = Paginator(publicacion, 40)
	try:
		publicaciones = paginator.page(page)
	except PageNotAnInteger:
		publicaciones = paginator.page(1)
	except EmptyPage:
		publicaciones = paginator.page(paginator.num_pages)
	return render(request, 'app/publicaciones_iiep.html', {'publicaciones': publicaciones})

def PublicacionIIEPDetalle(request, id): 
	publicacion = PublicacionIIEP.objects.using('iiep').get(id=id)
	contexto = {'publicacion': publicacion}
	return render (request, 'app/publicacion_detail_iiep.html', contexto)

def ProyectosIIEP(request):
	proyecto = ProyectoIIEP.objects.using('iiep').all().order_by('-id')
	page = request.GET.get('page', 1)
	paginator = Paginator(proyecto, 20)
	try:
		proyectos = paginator.page(page)
	except PageNotAnInteger:
		proyectos = paginator.page(1)
	except EmptyPage:
		proyectos = paginator.page(paginator.num_pages)
	return render(request, 'app/proyectos_iiep.html', {'proyectos':proyectos})

def ProyectoIIEPDetalle(request, id):
	proyecto = ProyectoIIEP.objects.using('iiep').get(id=id)
	contexto = {'proyecto':proyecto}
	return render(request, 'app/proyecto_detail_iiep.html', contexto)

def ActividadesIIEP(request):
	evento = ActividadIIEP.objects.using('iiep').all().order_by('-id')
	page = request.GET.get('page', 1)
	paginator = Paginator(evento, 20)
	try:
		eventos = paginator.page(page)
	except PageNotAnInteger:
		eventos = paginator.page(1)
	except EmptyPage:
		eventos = paginator.page(paginator.num_pages)
	return render(request, 'app/actividades_iiep.html', {'eventos':eventos})

def ActividadIIEPDetalle(request, id): 
	evento = ActividadIIEP.objects.using('iiep').get(id=id)
	contexto = {'evento':evento}
	return render (request, 'app/actividad_detail_iiep.html', contexto)
