from django.urls import path
from .views import *

urlpatterns=[
	path('investigadores/', InvestigadoresView.as_view(), name='investigadores-list'),
	path('investigador/<int:pk>', InvestigadorDetalleView.as_view(), name="investigador-detalle"),
]

urlpatterns+=[
	# path('publicaciones/', PublicacionesView.as_view(), name='publicaciones-list'),
	path('publicaciones/<str:cat>', PublicacionesView, name='publicaciones-list'),
	path('publicacion/<int:pk>', PublicacionDetalleView.as_view(), name="publicacion-detalle"),
	path('publicaciones/iiep/', PublicacionesIIEP, name='publicaciones-iiep'),
	path('publicacion/iiep/<int:id>', PublicacionIIEPDetalle, name='publicacion-iiep-detalle'),
]

urlpatterns+=[
	path('proyectos/', ProyectosView.as_view(), name='proyectos-list'),
	path('proyecto/<int:pk>', ProyectoDetalleView.as_view(), name="proyecto-detalle"),
	path('proyectos/iiep/', ProyectosIIEP, name='proyectos-iiep'),
	path('proyecto/iiep/<int:id>', ProyectoIIEPDetalle, name='proyecto-iiep-detalle'),
]

urlpatterns+=[
	path('actividades/', ActividadesView.as_view(), name='actividades-list'),
	path('actividad/<int:pk>', ActividadDetalleView.as_view(), name="actividad-detalle"),
	path('actividades/iiep/', ActividadesIIEP, name='actividades-iiep'),
	path('actividad/iiep/<int:id>', ActividadIIEPDetalle, name='actividad-iiep-detalle'),
]

urlpatterns+=[
	path('novedades/', NovedadesView, name='novedades-list'),
	path('novedad/<int:pk>', NovedadDetalleView.as_view(), name="novedad-detalle"),
]

urlpatterns+=[
	# path('datos/', DatosView.as_view(), name='datos-list'),
	path('datos/<str:cat>', DatosView, name='datos-list'),
	path('dato/<int:pk>', DatoDetalleView.as_view(), name="dato-detalle"),
]