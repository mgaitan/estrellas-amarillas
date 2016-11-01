from django.shortcuts import render, redirect
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
            cnt = prev_data['cantidad_de_victimas_fatales']
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


def Map(request):
    return render(request, 'data/map.html',)


def tablero(request):
    siniestros = Siniestro.objects.all().order_by('-id')
    victimas = Victima.objects.all()
    if request.method == 'POST':
        return redirect('registro/')
    return render(request, 'tablasiniestro.html',
        {'victimas': victimas,
        'siniestros': siniestros,
        })

