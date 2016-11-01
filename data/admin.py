from django.contrib import admin
from .models import Causa, Siniestro, Victima
# Register your models here.

class Tablas_Admin(admin.ModelAdmin):
	model = Siniestro
	list_display= ("causa_principal","provincia")
	list_filter=("provincia","causa_principal")

class Datos_Admin(admin.ModelAdmin):
	model= Victima
	list_display= ("siniestro","apellido","nombres","genero",)
	list_filter=("genero",)

admin.site.register(Causa)
admin.site.register(Siniestro,Tablas_Admin)
admin.site.register(Victima,Datos_Admin)