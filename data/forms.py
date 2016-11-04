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

	#import pdb; pdb.set_trace()
	#def clean_fecha(self):
	#	fecha = self.cleaned_data['date']
		#if fecha < datetime.date.today():
			#raise forms.ValidationError("The date cannot be in the past!")
		#return fecha


	class Meta:
		model = Victima
		fields = ['nombres', 'apellido', 'fecha', 'dni', 'nacionalidad', 
				  'lugar_residencia', 'genero', 'fecha_nacimiento']

class Buscador(forms.Form):
	busqueda= forms.CharField(max_length = 15)
	

VictimaFormSet = inlineformset_factory(Siniestro, Victima, form=VictimaForm, extra=1)
