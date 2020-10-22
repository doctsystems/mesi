from django.db import models
from django.urls import reverse

class Investigador(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	palabras_clave = models.CharField(max_length=50, null=True)
	titulo_grado_espanol = models.CharField(max_length=50)
	texto_espanol = models.CharField(max_length=500)
	texto_corto_espanol = models.CharField(max_length=250, null=True)
	institucion_grado = models.CharField(max_length=100)
	foto = models.ImageField()
	cv_espanol = models.FileField(upload_to='cv', null=True)

	class Meta:
		verbose_name_plural = "Investigadores IIEP"
		db_table = 'investigadores'

	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellido)

class Publicacion(models.Model):
	titulo_ingles = models.CharField(max_length=255, blank=True, null=True)
	investigador_id = models.IntegerField(blank=True, null=True)
	subarea_id = models.PositiveIntegerField(blank=True, null=True)
	texto_ingles = models.TextField(blank=True, null=True)
	titulo_espanol = models.CharField(max_length=255, blank=True, null=True)
	texto_espanol = models.TextField(blank=True, null=True)
	cita_bibliografica = models.CharField(max_length=255, blank=True, null=True)
	palabras_clave = models.CharField(max_length=255, blank=True, null=True)
	fecha = models.IntegerField(blank=True, null=True)
	activo = models.IntegerField(blank=True, null=True)
	destacado = models.IntegerField(blank=True, null=True)
	es_iiep = models.IntegerField(blank=True, null=True)
	creator_id = models.IntegerField(blank=True, null=True)
	creator_date = models.IntegerField(blank=True, null=True)
	last_update_id = models.IntegerField(blank=True, null=True)
	last_update_date = models.IntegerField(blank=True, null=True)
	eliminado = models.IntegerField(blank=True, null=True)
	orden = models.IntegerField(blank=True, null=True)
	director_id = models.IntegerField(blank=True, null=True)
	categoria_id = models.IntegerField(blank=True, null=True)
	id_viejo = models.IntegerField(blank=True, null=True)
	institucion_id = models.IntegerField(blank=True, null=True)
	numero = models.CharField(max_length=10, blank=True, null=True)
	investigador = models.ManyToManyField(Investigador, db_table="investigadores_publicaciones")

	class Meta:
		verbose_name_plural = "Publicaciones IIEP"
		managed = False
		db_table = 'publicaciones'

	def __str__(self):
		return '{}'.format(self.titulo_espanol)

	def get_absolute_url(self):
		return reverse('app:publicacion-iiep-detalle', args=[str(self.id)])

class Proyecto(models.Model):
	titulo_espanol = models.CharField(max_length=255, blank=True, null=True)
	descripcion_espanol = models.TextField(blank=True, null=True)
	titulo_ingles = models.CharField(max_length=255, blank=True, null=True)
	descripcion_ingles = models.TextField(blank=True, null=True)
	activo = models.IntegerField(blank=True, null=True)
	orden = models.IntegerField(blank=True, null=True)
	creator_id = models.IntegerField(blank=True, null=True)
	creator_date = models.IntegerField(blank=True, null=True)
	last_update_id = models.IntegerField(blank=True, null=True)
	last_update_date = models.IntegerField(blank=True, null=True)
	eliminado = models.IntegerField(blank=True, null=True)
	director_id = models.IntegerField(blank=True, null=True)
	palabras_clave = models.CharField(max_length=500, blank=True, null=True)
	investigador = models.ManyToManyField(Investigador, db_table="investigadores_proyectos")

	class Meta:
		verbose_name_plural = "Proyectos IIEP"
		managed = False
		db_table = 'proyectos'

	def __str__(self):
		return '{}'.format(self.titulo_espanol)

	def get_absolute_url(self):
		return reverse('app:proyecto-iiep-detalle', args=[str(self.id)])

class Evento(models.Model):
	titulo_espanol = models.CharField(max_length=255, blank=True, null=True)
	texto_espanol = models.TextField(blank=True, null=True)
	copete_espanol = models.CharField(max_length=255, blank=True, null=True)
	titulo_ingles = models.CharField(max_length=255, blank=True, null=True)
	texto_ingles = models.TextField(blank=True, null=True)
	copete_ingles = models.CharField(max_length=255, blank=True, null=True)
	investigador_id = models.IntegerField(blank=True, null=True)
	fecha = models.IntegerField(blank=True, null=True)
	hora = models.CharField(max_length=255, blank=True, null=True)
	lugar = models.CharField(max_length=255, blank=True, null=True)
	creator_id = models.IntegerField(blank=True, null=True)
	creator_date = models.IntegerField(blank=True, null=True)
	last_update_id = models.IntegerField(blank=True, null=True)
	last_update_date = models.IntegerField(blank=True, null=True)
	activo = models.IntegerField(blank=True, null=True)
	destacado = models.IntegerField(blank=True, null=True)
	eliminado = models.IntegerField(blank=True, null=True)
	orden = models.IntegerField(blank=True, null=True)
	evento_tipo_id = models.PositiveIntegerField(blank=True, null=True)
	fecha_hasta = models.IntegerField(blank=True, null=True)
	investigador = models.ManyToManyField(Investigador, db_table="evento_investigador")

	class Meta:
		verbose_name_plural = "Actividades IIEP"
		managed = False
		db_table = 'eventos'

	def __str__(self):
		return '{}'.format(self.titulo_espanol)

	def get_absolute_url(self):
		return reverse('app:actividad-iiep-detalle', args=[str(self.id)])
