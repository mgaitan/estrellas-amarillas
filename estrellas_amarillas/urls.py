"""estrellas_amarillas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from djgeojson.views import GeoJSONLayerView
from django.conf.urls import url, include
from django.contrib import admin
from data.models import Siniestro
from data.views import alta_siniestro, alta_victima, Map, SiniestroWizard


urlpatterns = [
    url(r'^$', SiniestroWizard.as_view(), name='home'),
    url(r'^siniestro/(?P<id_siniestro>[0-9]+)/alta-victima', alta_victima, name='alta-victima'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Siniestro), name='geojson'),
    url(r'^admin/', admin.site.urls),
    url(r'^map/', Map, name='map'),
    url(r'^account/', include("account.urls")),
]
