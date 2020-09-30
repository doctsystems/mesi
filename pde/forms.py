from django import forms
from .models import *

class RegMIPForm(forms.ModelForm):

	class Meta:
		model = RegMIP
		fields = ('nacional', 'regional', 'sector')

		# widgets = {
		# 	'nacional': forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'})),
		# 	'regional': forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'})),
		# 	'sector': forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'})),            
		# }

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
				})
