from django import forms
from .models import Siniestro, Victima

class SiniestroForm(forms.ModelForm):
	class Meta:
		model = Siniestro
		fields = ['fecha', 'hora', 'lugar', 'provincia', 'posicion', 'causa_principal', 'mensaje']


class VictimaForm(forms.ModelForm):
	class Meta:
		model = Victima
		fields = ['nombres', 'apellido', 'fecha', 'dni', 'nacionalidad', 
				  'lugar_residencia', 'genero', 'fecha_nacimiento']
