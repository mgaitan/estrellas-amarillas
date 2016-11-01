from django import forms
# from bootstrap3_datepicker.fields import DatePickerField
from bootstrap_datepicker.widgets import DatePicker
from django.forms import inlineformset_factory
from .models import Siniestro, Victima


class SiniestroForm(forms.ModelForm):
    fecha = forms.DateField(widget=DatePicker(options={"format": "dd/mm/yyyy", "autoclose": True}), input_formats=['%d/%m/%Y'])
    cantidad_de_victimas_fatales = forms.IntegerField(min_value=1)

    class Meta:
        model = Siniestro
        fields = ['lugar', 'provincia', 'posicion', 'fecha', 'causa_principal', 'mensaje']


class VictimaForm(forms.ModelForm):
    fecha = forms.DateField(widget=DatePicker(options={"format": "dd/mm/yyyy", "autoclose": True}), input_formats=['%d/%m/%Y'])
    fecha_nacimiento = forms.DateField(widget=DatePicker(options={"format": "dd/mm/yyyy", "autoclose": True}), input_formats=['%d/%m/%Y'])

    class Meta:
        model = Victima
        fields = ['nombres', 'apellido', 'fecha', 'dni', 'nacionalidad',
                  'lugar_residencia', 'genero', 'fecha_nacimiento']


VictimaFormSet = inlineformset_factory(Siniestro, Victima, form=VictimaForm, extra=1)
