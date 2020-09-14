from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey
from ckeditor.fields import RichTextField

class ModeloBase(models.Model):
	estado = models.BooleanField(default=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)
	usuario_creacion = UserForeignKey(auto_user_add=True, related_name='+')
	usuario_modificacion = UserForeignKey(auto_user=True, related_name='+')

	class Meta:
		abstract=True

class SiteSettings(ModeloBase):
	titulo = models.CharField(max_length=300, default="Titulo del sitio")
	copete = RichTextField(help_text="Copete", default="Copete del sitio", null=True, blank=True)
	desarrollo = RichTextField(help_text="Descripcion del sitio", default="Descripcion del sitio")

	class Meta:
		verbose_name_plural = "Institucional"

	def __str__(self):
		return 'Configuraciones'

	def get_absolute_url(self):
		return reverse('core:institucional', args=[str(self.id)])

