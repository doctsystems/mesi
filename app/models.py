from django.db import models
from core.models import ModeloBase
from stdimage import StdImageField
from django.urls import reverse
from ckeditor.fields import RichTextField

class Investigador(ModeloBase):
	tipos=(
		('nn', '----------'),
		('inv', 'Investigador/a'),
		('aso', 'Asociado/a'),
		('bec', 'Becario/a'),
		('aux', 'Auxiliar'),
		('otr', 'Otro/a'),
	)
	tipo = models.CharField(max_length=3, choices=tipos, default='nn')
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	perfil = models.CharField(max_length=100)
	biografia = RichTextField(help_text="Biografia")
	avatar = StdImageField(upload_to='investigadores/img/avatar/',
		variations={'thumbnail': {"width": 240, "height": 200, "crop": True}},
		null=True, blank=True)
	email = models.EmailField(max_length=254, default="email@example.com")
	curriculum = models.FileField(upload_to="investigadores/cv/")
	orcid = models.CharField(max_length=30, help_text="Numero ORCID (xxxx-xxxx-xxxx-xxxx)")
	link = models.URLField(max_length = 200, help_text="Link al perfil privado")

	class Meta:
		verbose_name = "integrante"
		verbose_name_plural = "Integrantes"

	def __str__(self):
		return '{} {}'.format(self.nombres, self.apellidos)

	def save(self):
		self.nombres=self.nombres.upper()
		self.apellidos=self.apellidos.upper()
		super(Investigador, self).save()

	def get_absolute_url(self):
		return reverse('app:investigador-detalle', args=[str(self.id)])

class Publicacion(ModeloBase):
	tipos=(
		('nn', '----------'),
		('not', 'Notas'),
		('inf', 'Informes Tecnicos'),
		('pub', 'Publicaciones Academicas'),
		('tes', 'Tesis'),
		('otr', 'Otro'),
	)
	categoria = models.CharField(max_length=3, choices=tipos, default='nn')
	titulo = models.CharField(max_length=300, null=True, blank=True, help_text="Titulo de la Publicacion")
	fecha = models.DateField(help_text="Fecha de publicacion")
	copete = RichTextField(help_text="Copete", null=True, blank=True)
	desarrollo = RichTextField(help_text="Contenido de la publicacion")
	imagen = StdImageField(upload_to='publicaciones/img/',
		variations={'thumbnail': {"width": 240, "height": 200, "crop": True}},
		null=True, blank=True)
	video = models.FileField(upload_to="publicaciones/video/", null=True, blank=True)
	integrantes = models.ManyToManyField(Investigador)
	medios = models.CharField(max_length=100, null=True, blank=True)
	link = models.URLField(max_length=200, null=True, blank=True, help_text="Link al medio")
	es_novedad = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = "Publicaciones MESI"

	def __str__(self):
		return '{}'.format(self.titulo)

	def get_absolute_url(self):
		return reverse('app:publicacion-detalle', args=[str(self.id)])

class Proyecto(ModeloBase):
	titulo = models.CharField(max_length=300, help_text="Titulo del Proyecto")
	fecha_inicio = models.DateField(help_text="Fecha de inicio")
	fecha_final = models.DateField(help_text="Fecha de finalizacion", null=True, blank=True)
	desarrollo = RichTextField(help_text="Descripcion del proyecto")
	terminado = models.BooleanField(default=False)
	integrantes = models.ManyToManyField(Investigador)

	class Meta:
		verbose_name_plural = "Proyectos"

	def __str__(self):
		return '{}'.format(self.titulo)

	def get_absolute_url(self):
		return reverse('app:proyecto-detalle', args=[str(self.id)])

class Actividad(ModeloBase):
	titulo = models.CharField(max_length=300, help_text="Titulo del evento")
	fecha_inicio = models.DateField(help_text="Fecha de inicio")
	fecha_final = models.DateField(help_text="Fecha de finalizacion", null=True, blank=True)
	hora_inicio = models.TimeField(help_text="Hora de inicio")
	hora_final = models.TimeField(help_text="Hora de finalizacion", null=True, blank=True)
	lugar = models.CharField(max_length=100, help_text="Lugar del evento")
	desarrollo = RichTextField(help_text="Descripcion de la actividad")
	integrantes = models.ManyToManyField(Investigador)

	class Meta:
		verbose_name_plural = "Actividades"

	def __str__(self):
		return '{}'.format(self.titulo)

	def get_absolute_url(self):
		return reverse('app:actividad-detalle', args=[str(self.id)])

class Novedad(ModeloBase):
	titulo = models.CharField(max_length=300)
	fecha = models.DateField(help_text="Fecha de ocurrencia")
	copete = RichTextField(help_text="Copete", null=True, blank=True)
	desarrollo = RichTextField(help_text="Descripcion de la novedad")
	imagen = StdImageField(upload_to='novedades/img/', 
		variations={'thumbnail': {"width": 240, "height": 200, "crop": True}},
		null=True, blank=True)
	link = models.URLField(max_length = 200, help_text="Link de la presentacion")

	class Meta:
		verbose_name_plural = "Novedades"

	def __str__(self):
		return '{}'.format(self.titulo)

	def get_absolute_url(self):
		return reverse('app:novedad-detalle', args=[str(self.id)])

class Dato(ModeloBase):
	tipos=(
		('nn', '----------'),
		('ene', 'Energia y ambiente'),
		('sec', 'Datos sectoriales'),
		('mat', 'Datos matriciales'),
		('com', 'Comercio'),
		# ('otr', 'Otro'),
	)
	categoria = models.CharField(max_length=3, choices=tipos, default='nn')
	fecha = models.DateField(help_text="Fecha...")
	titulo = models.CharField(max_length=300, help_text="Titulo...")
	copete = RichTextField(help_text="Copete", null=True, blank=True)
	desarrollo = RichTextField(help_text="Descripcion...")
	imagen = StdImageField(upload_to='datos/img/', 
		variations={'thumbnail': {"width": 240, "height": 200, "crop": True}},
		null=True, blank=True)
	integrantes = models.ManyToManyField(Investigador)

	class Meta:
		verbose_name_plural = "Datos y Estadisticas"

	def __str__(self):
		return '{}'.format(self.titulo)

	def get_absolute_url(self):
		return reverse('app:dato-detalle', args=[str(self.id)])

class Archivo(ModeloBase):
	publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, null=True, blank=True)
	proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True, blank=True)
	actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, null=True, blank=True)
	novedad = models.ForeignKey(Novedad, on_delete=models.CASCADE, null=True, blank=True)
	dato = models.ForeignKey(Dato, on_delete=models.CASCADE, null=True, blank=True)
	descripcion = models.CharField(max_length=300, help_text="Titulo o nombre del archivo")
	archivo = models.FileField(upload_to="uploads/files/")

	class Meta:
		verbose_name_plural = "Archivos"

	def __str__(self):
		return '{}'.format(self.id)

class PublicacionIIEP(models.Model):
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

	class Meta:
		verbose_name_plural = "Publicaciones IIEP"
		managed = False
		db_table = 'publicaciones'

	def __str__(self):
		return '{}'.format(self.titulo_espanol)

	def get_absolute_url(self):
		return reverse('app:publicacion-iiep-detalle', args=[str(self.id)])

class ProyectoIIEP(models.Model):
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

	class Meta:
		verbose_name_plural = "Proyectos IIEP"
		managed = False
		db_table = 'proyectos'

	def __str__(self):
		return '{}'.format(self.titulo_espanol)

	def get_absolute_url(self):
		return reverse('app:proyecto-iiep-detalle', args=[str(self.id)])

class ActividadIIEP(models.Model):
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

	class Meta:
		verbose_name_plural = "Actividades IIEP"
		managed = False
		db_table = 'eventos'

	def __str__(self):
		return '{}'.format(self.titulo_espanol)

	def get_absolute_url(self):
		return reverse('app:actividad-iiep-detalle', args=[str(self.id)])
