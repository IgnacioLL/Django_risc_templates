from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
	name = forms.CharField(label="Nombre y apellidos del Cliente", required = True)


	class Meta:
		model = Cliente
		exclude = ["timestamp", ]



	def __init__(self, *args, **kwargs):
		super(ClienteForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({
		    'class': 'form-control'})
