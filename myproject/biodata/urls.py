from django.urls import path
from biodata.views import biodata

urlpatterns = [
    path('biodata/', biodata, name='biodata'),
]