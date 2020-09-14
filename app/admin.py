from django.contrib import admin
from .models import *
from django import forms
from django.utils.safestring import mark_safe

# Register your models here.
class InvestigadorAdmin(admin.ModelAdmin):
	exclude = ['estado']
	ordering = ('nombres', 'apellidos')
	list_display = ('foto', 'nombres', 'apellidos', 'tipo', 'link')
	# fields = ['nombres', 'apellidos', 'tipo_investigador', 'link']
	# readonly_fields = ('created', 'updated')

	def foto(self, obj):
		if obj.avatar:
			return mark_safe('<image src="%s" width="60" height="50" />' % obj.avatar.thumbnail.url)
		else:
			return mark_safe('<image src="/media/investigadores/img/avatar/male.png" width="60" height="60" />')
	foto.short_description = 'Foto'
	foto.allow_tags = True

class PublicacionAdmin(admin.ModelAdmin):
	exclude = ['estado']
	filter_horizontal = ('autores', 'asociados', )
	ordering = ('fecha', 'titulo')
	list_display = ('titulo', 'fecha', 'pub_autores', )
	search_fields = ('titulo','fecha','autores__nombres', 'autores__apellidos')
	# date_hierarchy = 'fecha'
	list_filter = ('fecha', 'autores__nombres','autores__apellidos')

	def pub_autores(self, obj):
		return ", ".join(
		[c.nombres for c in obj.autores.all().order_by("nombres")])
	pub_autores.short_description = "Autores"

class ProyectoAdmin(admin.ModelAdmin):
	exclude = ['estado', 'terminado']
	filter_horizontal = ('autores', 'asociados', )
	ordering = ('fecha_inicio', 'titulo')
	list_display = ('titulo', 'fecha_inicio', 'pub_autores', )
	search_fields = ('titulo','fecha_inicio','autores__nombres', 'autores__apellidos')
	list_filter = ('fecha_inicio', 'autores__nombres','autores__apellidos')

	def pub_autores(self, obj):
		return ", ".join(
		[c.nombres for c in obj.autores.all().order_by("nombres")])
	pub_autores.short_description = "Autores"

class ActividadAdmin(admin.ModelAdmin):
	exclude = ['estado']
	list_display = ('fecha_inicio', 'hora_inicio', 'lugar', 'descripcion', )

	def descripcion(self, obj):
		return mark_safe('%s' % obj.desarrollo)
	descripcion.short_description = 'Descripcion'
	descripcion.allow_tags = True

class NovedadAdmin(admin.ModelAdmin):
	exclude = ['estado']
	ordering = ('fecha', 'titulo')
	list_display = ('titulo', 'fecha',  'link', 'descripcion',)

	def descripcion(self, obj):
		return mark_safe('%s' % obj.copete)
	descripcion.short_description = 'Descripcion'
	descripcion.allow_tags = True

class DatoAdmin(admin.ModelAdmin):
	exclude = ['estado', ]
	filter_horizontal = ('autores', 'asociados', )
	ordering = ('fecha', 'titulo')
	list_display = ('titulo', 'fecha', 'dato_autores', 'descripcion' )
	search_fields = ('titulo','fecha','autores__nombres', 'autores__apellidos')
	list_filter = ('fecha', 'autores__nombres','autores__apellidos')

	def dato_autores(self, obj):
		return ", ".join(
		[c.nombres for c in obj.autores.all().order_by("nombres")])
	dato_autores.short_description = "Autores"

	def descripcion(self, obj):
		return mark_safe('%s' % obj.desarrollo)
	descripcion.short_description = 'Descripcion'
	descripcion.allow_tags = True

admin.site.register(Investigador, InvestigadorAdmin)
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Novedad, NovedadAdmin)
admin.site.register(Dato, DatoAdmin)
