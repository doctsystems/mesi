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