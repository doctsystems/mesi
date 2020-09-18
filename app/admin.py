from django.contrib import admin
from .models import *
from django import forms
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars

class InvestigadorAdmin(admin.ModelAdmin):
	exclude = ['estado']
	ordering = ('nombres', 'apellidos')
	list_display = ('foto', 'nombres', 'apellidos', 'tipo', 'link')

	def foto(self, obj):
		if obj.avatar:
			return mark_safe('<image src="%s" width="60" height="50" />' % obj.avatar.thumbnail.url)
		else:
			return mark_safe('<image src="/media/investigadores/img/avatar/male.png" width="60" height="60" />')
	foto.short_description = 'Foto'
	foto.allow_tags = True

class ArchivoPublicacionInline(admin.StackedInline): #TabularInline
	exclude = ['estado', 'actividad', 'proyecto', 'novedad', 'dato']
	model = Archivo

class PublicacionAdmin(admin.ModelAdmin):
	exclude = ['estado']
	ordering = ('fecha', 'titulo')
	list_display = ('titulo', 'fecha', 'pub_integrantes', )
	search_fields = ('titulo','fecha','integrantes__nombres', 'integrantes__apellidos')
	list_filter = ('fecha', 'integrantes__nombres','integrantes__apellidos')
	filter_horizontal = ('integrantes', )
	inlines = [ArchivoPublicacionInline]

	def pub_integrantes(self, obj):
		return ", ".join(
		[c.nombres for c in obj.integrantes.all().order_by("nombres")])
	pub_integrantes.short_description = "Integrantes"

class ArchivoProyectoInline(admin.StackedInline):
	exclude = ['estado', 'actividad', 'publicacion', 'novedad', 'dato']
	model = Archivo

class ProyectoAdmin(admin.ModelAdmin):
	exclude = ['estado', 'terminado']
	ordering = ('fecha_inicio', 'titulo')
	list_display = ('titulo', 'fecha_inicio', 'pub_integrantes', 'terminado')
	search_fields = ('titulo','fecha_inicio','integrantes__nombres', 'integrantes__apellidos')
	list_filter = ('fecha_inicio', 'integrantes__nombres','integrantes__apellidos')
	filter_horizontal = ('integrantes', )
	inlines = [ArchivoProyectoInline]

	def pub_integrantes(self, obj):
		return ", ".join(
		[c.nombres for c in obj.integrantes.all().order_by("nombres")])
	pub_integrantes.short_description = "Autores"

	def save_model(self, request, obj, form, change):
		if request.POST['fecha_final']:
			print('Terminado...')
			obj.terminado=True
		else:
			print('No terminado...')
			obj.terminado=False
		return super(ProyectoAdmin, self).save_model(request, obj, form, change)

class ArchivoActividadInline(admin.StackedInline):
	exclude = ['estado', 'publicacion', 'proyecto', 'novedad', 'dato']
	model = Archivo

class ActividadAdmin(admin.ModelAdmin):
	exclude = ['estado']
	filter_horizontal = ('integrantes', )
	list_display = ('titulo', 'fecha_inicio', 'hora_inicio', 'lugar', )
	inlines = [ArchivoActividadInline]

class ArchivoNovedadInline(admin.StackedInline):
	exclude = ['estado', 'publicacion', 'proyecto', 'actividad', 'dato']
	model = Archivo

class NovedadAdmin(admin.ModelAdmin):
	exclude = ['estado']
	ordering = ('fecha', 'titulo')
	list_display = ('titulo', 'fecha',  'link', )
	inlines = [ArchivoNovedadInline]

	def descripcion(self, obj):
		return mark_safe('%s' % obj.copete)
	descripcion.short_description = 'Descripcion'
	descripcion.allow_tags = True

class ArchivoDatoInline(admin.StackedInline):
	exclude = ['estado', 'publicacion', 'proyecto', 'actividad', 'novedad']
	model = Archivo

class DatoAdmin(admin.ModelAdmin):
	exclude = ['estado', ]
	filter_horizontal = ('integrantes', )
	ordering = ('fecha', 'titulo')
	list_display = ('titulo', 'fecha', 'dato_integrantes', )
	search_fields = ('titulo','fecha','integrantes__nombres', 'integrantes__apellidos')
	list_filter = ('fecha', 'integrantes__nombres','integrantes__apellidos')
	inlines = [ArchivoDatoInline]

	def dato_integrantes(self, obj):
		return ", ".join(
		[c.nombres for c in obj.integrantes.all().order_by("nombres")])
	dato_integrantes.short_description = "Integrantes"

admin.site.register(Investigador, InvestigadorAdmin)
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Novedad, NovedadAdmin)
admin.site.register(Dato, DatoAdmin)
