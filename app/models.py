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
	email = models.EmailField(max_length=254, default="email@example.com")
	biografia = RichTextField(help_text="Biografia")
	avatar = StdImageField(upload_to='investigadores/img/avatar/',
		variations={'thumbnail': {"width": 240, "height": 200, "crop": True}},
		null=True, blank=True)
	curriculum = models.FileField(upload_to="investigadores/cv/", null=True, blank=True)
	orcid = models.CharField(max_length=30, help_text="Numero ORCID (xxxx-xxxx-xxxx-xxxx)", null=True, blank=True)
	link = models.URLField(max_length = 200, help_text="Link al perfil privado", null=True, blank=True)

	class Meta:
		ordering = ['apellidos', ]
		verbose_name = "integrante"
		verbose_name_plural = "Integrantes"

	def __str__(self):
		return '{}, {}'.format(self.apellidos, self.nombres)

	# def save(self):
	# 	self.nombres=self.nombres.upper()
	# 	self.apellidos=self.apellidos.upper()
	# 	super(Investigador, self).save()

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
	titulo = models.CharField(max_length=300, help_text="Titulo de la Publicacion")
	fecha = models.DateField(help_text="Fecha de publicacion")
	cita_APA = RichTextField(help_text="cita_APA", null=True, blank=True)
	resumen_Abstract = RichTextField(help_text="Contenido de la publicacion")
	imagen = StdImageField(upload_to='publicaciones/img/',
		variations={'thumbnail': {"width": 240, "height": 200, "crop": True}},
		null=True, blank=True)
	video = models.FileField(upload_to="publicaciones/video/", null=True, blank=True)
	integrantes = models.ManyToManyField(Investigador)
	medios = models.CharField(max_length=100, null=True, blank=True)
	link = models.URLField(max_length=200, null=True, blank=True, help_text="Link al medio")
	doi = models.URLField(max_length=200, null=True, blank=True, help_text="Link DOI")
	es_novedad = models.BooleanField(default=False)

	class Meta:
		ordering = ['-fecha', ]
		verbose_name_plural = "Publicaciones MESI"

	def __str__(self):
		return '{}'.format(self.titulo)

	def get_absolute_url(self):
		return reverse('app:publicacion-detalle', args=[str(self.id)])

class Proyecto(ModeloBase):
	titulo = models.CharField(max_length=300, help_text="Titulo del Proyecto")
	fecha_inicio = models.DateField(help_text="Fecha de inicio")
	fecha_final = models.DateField(help_text="Fecha de finalizacion", null=True, blank=True)
	resumen_Abstract = RichTextField(help_text="Descripcion del proyecto")
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
	resumen_Abstract = RichTextField(help_text="Descripcion de la actividad")
	integrantes = models.ManyToManyField(Investigador)
	link = models.URLField(max_length=200, help_text="Formulario de registro", null=True, blank=True)
	logo = StdImageField(upload_to='actividades/logos/',
		variations={'thumbnail': {"width": 240, "height": 200, "crop": True}},
		null=True, blank=True)
	flyer = StdImageField(upload_to='actividades/flyers/',
		variations={'thumbnail': {"width": 240, "height": 200, "crop": True}},
		null=True, blank=True)

	class Meta:
		verbose_name_plural = "Actividades"

	def __str__(self):
		return '{}'.format(self.titulo)

	def get_absolute_url(self):
		return reverse('app:actividad-detalle', args=[str(self.id)])

class Novedad(ModeloBase):
	titulo = models.CharField(max_length=300)
	fecha = models.DateField(help_text="Fecha de ocurrencia")
	cita_APA = RichTextField(help_text="cita_APA", null=True, blank=True)
	resumen_Abstract = RichTextField(help_text="Descripcion de la novedad")
	imagen = StdImageField(upload_to='novedades/img/', 
		variations={'thumbnail': {"width": 240, "height": 200, "crop": True}},
		null=True, blank=True)
	link = models.URLField(max_length = 200, help_text="Link de la presentacion")

	class Meta:
		ordering = ['-fecha', ]
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
	cita_APA = RichTextField(help_text="cita_APA", null=True, blank=True)
	resumen_Abstract = RichTextField(help_text="Descripcion...")
	imagen = StdImageField(upload_to='datos/img/', 
		variations={'thumbnail': {"width": 240, "height": 200, "crop": True}},
		null=True, blank=True)
	integrantes = models.ManyToManyField(Investigador)

	class Meta:
		ordering = ['-fecha', ]
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
