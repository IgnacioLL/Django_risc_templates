from django import forms
from .models import tarifas

class tarifasForm(forms.ModelForm):
	name = forms.CharField(label="Nombre de la tarifa", required = True)
	comision_de_la_tarifa = forms.FloatField(label="Comision de la tarifa (%)")
 
	class Meta:
		model = tarifas
		exclude = ["timestamp", ]



	def __init__(self, *args, **kwargs):
		super(tarifasForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({
		    'class': 'form-control'})
