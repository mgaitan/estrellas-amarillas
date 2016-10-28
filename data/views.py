from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Siniestro, Victima
from .forms import SiniestroForm, VictimaForm, VictimaFormSet


# Create your views here.

def alta_siniestro(request):
	form = SiniestroForm()
	formset = VictimaFormSet()
	if request.method == 'POST':
		form = SiniestroForm(request.POST)
		if form.is_valid():
			siniestro = form.save()
			formset = VictimaFormSet(request.POST, request.FILES, instance=siniestro)
			if formset.is_valid():
				formset.save()
				messages.info(request, 'Su información ha sido registrada. ¡Gracias por su ayuda!')
				return redirect('registro/') 
			else:
				messages.warning(request, 'Hay errores en la carga. Por favor, corrijalos')
				siniestro.delete()
		else:
			messages.warning(request, 'Hay errores en la carga. Por favor, corrijalos')
	return render(request, 'data/form.html', {'form': form, 'titulo': 'Reportar Siniestro', 'formset': formset})


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


def tablero(request):
	siniestros = Siniestro.objects.all()
	victimas = Victima.objects.all()
	if request.method == 'POST':
		return redirect('registro/')
	return render(request, 'tablasiniestro.html',
		{'victimas': victimas,
		'siniestros': siniestros,
		}) 
