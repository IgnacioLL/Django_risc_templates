from django import forms
from .models import elementos

class elementosForm(forms.ModelForm):
	name = forms.CharField(label="Direccion y numero del inmueble", required = True)


	class Meta:
		model = elementos
		exclude = ["timestamp", ]



	def __init__(self, *args, **kwargs):
		super(elementosForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({
		    'class': 'form-control'})
