from django import forms
from .models import Encargo

class EncargoForm(forms.ModelForm):
	nif = forms.CharField(label="NIF", required = False)
	name = forms.CharField(label="Descripcion")

	class Meta:
		model = Encargo
		exclude = ["timestamp", ]
		widgets = {
			'documentacion': forms.Textarea(attrs={'rows':4, 'cols':15}),

		}


	def __init__(self, *args, **kwargs):
		super(EncargoForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({
		    'class': 'form-control'})
