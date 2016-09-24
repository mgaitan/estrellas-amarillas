from django.contrib import admin
from .models import Causa, Siniestro, Victima
# Register your models here.

admin.site.register(Causa)
admin.site.register(Siniestro)
admin.site.register(Victima)