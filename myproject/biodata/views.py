from django.shortcuts import render
from .forms import BiodataForm

def biodata(request):
    form = BiodataForm()
    return render(request, 'biodata.html', {'form': form})
