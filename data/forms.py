from django import forms
#from bootstrap3_datepicker.fields import DatePickerField
#from bootstrap3_datepicker.widgets import DatePickerInput
from django.forms import inlineformset_factory
from .models import Siniestro, Victima


class SiniestroForm(forms.ModelForm):

	#fecha = forms.DateField(widget=DatePickerInput())

	class Meta:
		model = Siniestro
		fields = ['lugar', 'provincia', 'posicion', 'fecha', 'causa_principal', 'mensaje']


class VictimaForm(forms.ModelForm):
	class Meta:
		model = Victima
		fields = ['nombres', 'apellido', 'fecha', 'dni', 'nacionalidad', 
				  'lugar_residencia', 'genero', 'fecha_nacimiento']


VictimaFormSet = inlineformset_factory(Siniestro, Victima, form=VictimaForm)
