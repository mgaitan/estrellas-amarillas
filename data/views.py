from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from formtools.wizard.views import SessionWizardView
from .models import Siniestro, Victima
from .forms import SiniestroForm, VictimaForm, VictimaFormSet
from django.forms import modelformset_factory


# Create your views here.

class SiniestroWizard(SessionWizardView):
    template_name = 'data/form.html'
    form_list = [SiniestroForm, VictimaFormSet]

    def get_form(self, step=None, data=None, files=None):
        if step is None:
            step = self.steps.current
        if step == "1":
            prev_data = self.get_cleaned_data_for_step('0')
            cnt = prev_data['cantidad_de_victimas_fatales']     #use appropriate key as per your form
            kwargs = self.get_form_kwargs(step)
            kwargs.update({
                'data': data,
                'files': files,
                'queryset': Victima.objects.none()
            })
            return modelformset_factory(Victima, VictimaForm, extra=cnt, max_num=cnt)(**kwargs)

        return super().get_form(step, data, files)

    def done(self, form_list, **kwargs):
        form_list = [f for f in form_list]
        siniestro = form_list[0].save()
        victimas = form_list[1].save(commit=False)
        for victima in victimas:
            victima.siniestro = siniestro
            victima.save()
        messages.info(self.request, 'Su información ha sido registrada. ¡Gracias por su ayuda!')
        return redirect('home')



def alta_siniestro(request):
    form = SiniestroForm()
    formset = VictimaFormSet()
    if request.method == 'POST':
        form = SiniestroForm(request.POST)
        if form.is_valid():

            formset = VictimaFormSet(request.POST, request.FILES, instance=siniestro, prefix='victimas')
            if formset.is_valid():
                formset.save()
                messages.info(request, 'Su información ha sido registrada. ¡Gracias por su ayuda!')
                return redirect('home')
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

def Map(request):
    return render(request, 'data/map.html',)
