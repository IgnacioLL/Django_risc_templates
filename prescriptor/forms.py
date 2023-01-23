from django import forms
from .models import Prescriptor

class PrescriptorForm(forms.ModelForm):
	name = forms.CharField(label="Nombre y apellidos del Prescriptor", required = True)


	class Meta:
		model = Prescriptor
		exclude = ["timestamp", ]



	def __init__(self, *args, **kwargs):
		super(PrescriptorForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({
		    'class': 'form-control'})
