from django.shortcuts import render, get_object_or_404, redirect
from .models import Siniestro
from .forms import SiniestroForm, VictimaForm

# Create your views here.

def alta_siniestro(request):
	form = SiniestroForm()
	if request.method == 'POST':
		form = SiniestroForm(request.POST)
		if form.is_valid():
			siniestro = form.save()
			return redirect('alta-victima', id_siniestro=siniestro.id) 
	return render(request, 'data/form.html', {'form': form, 'titulo': 'Reportar Siniestro'})


def alta_victima(request, id_siniestro):
	siniestro = get_object_or_404(Siniestro, id=id_siniestro)
	form = VictimaForm()
	if request.method == 'POST':
		form = VictimaForm(request.POST)
		if form.is_valid():
			victima = form.save(commit=False)
			victima.siniestro = siniestro
			victima.save()
			return redirect('alta-victima', id_siniestro=siniestro.id) 
	return render(request, 'data/form.html', {'form': form, 'titulo': 'Reportar Victima', 'siniestro': siniestro})