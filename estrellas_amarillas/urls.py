from djgeojson.views import GeoJSONLayerView
from django.conf.urls import url, include
from django.contrib import admin
from data.models import Siniestro
from data.views import Map, SiniestroWizard, tablero


urlpatterns = [
    url(r'^$', tablero, name='home'),
    url(r'^registro/', SiniestroWizard.as_view(), name='registro'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Siniestro), name='geojson'),
    url(r'^admin/', admin.site.urls),
    url(r'^map/', Map, name='map'),
    url(r'^account/', include("account.urls")),
]

