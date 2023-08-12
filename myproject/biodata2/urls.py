from django.urls import path
from .views import biodata, success

urlpatterns = [
    path('', biodata, name='biodata'),
    path('success/', success, name='success'),
]