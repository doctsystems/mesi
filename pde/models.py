from django.db import models

# Create your models here.
class RegMIP(models.Model):
	nacional=models.FileField(upload_to="uploads/files/in/")
	regional=models.FileField(upload_to="uploads/files/in/")
	sector=models.FileField(upload_to="uploads/files/in/")

	class Meta:
		verbose_name_plural = "Archivos"

	def __str__(self):
		return '{}'.format(self.id)

class VideoTutorial(models.Model):
	titulo=models.CharField(max_length=50, help_text="Titulo del video")
	link=models.URLField(max_length = 200, help_text="Link del video")
	tutorial=models.FileField(upload_to="publicaciones/tutoriales/", null=True, blank=True)

	class Meta:
		verbose_name_plural="Tutorial"

	def __str__(self):
		return '{}'.format(self.titulo)