from django import forms
#from bootstrap3_datepicker.fields import DatePickerField
#from bootstrap3_datepicker.widgets import DatePickerInput
from django.forms import inlineformset_factory
from .models import Siniestro, Victima
from bootstrap3_datetime.widgets import DateTimePicker


class SiniestroForm(forms.ModelForm):
	fecha =forms.DateField(
		widget=DateTimePicker(options={"format": "YYYY-MM-DD",
										"pickTime": False}))

	class Meta:
		model = Siniestro
		fields = ['lugar', 'provincia', 'posicion', 'fecha', 'causa_principal', 'mensaje']


class VictimaForm(forms.ModelForm):
	fecha_nacimiento = forms.DateField(
		widget=DateTimePicker(options={"format": "YYYY-MM-DD",
										"pickTime": False}))
	fecha =forms.DateField(
		widget=DateTimePicker(options={"format": "YYYY-MM-DD",
										"pickTime": False}))

	class Meta:
		model = Victima
		fields = ['nombres', 'apellido', 'fecha', 'dni', 'nacionalidad', 
				  'lugar_residencia', 'genero', 'fecha_nacimiento']


VictimaFormSet = inlineformset_factory(Siniestro, Victima, form=VictimaForm, extra=1)
