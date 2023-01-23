from django import forms
from .models import tarifas

class tarifasForm(forms.ModelForm):
	name = forms.CharField(label="Direccion y numero del inmueble", required = True)


	class Meta:
		model = tarifas
		exclude = ["timestamp", ]



	def __init__(self, *args, **kwargs):
		super(tarifasForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({
		    'class': 'form-control'})
