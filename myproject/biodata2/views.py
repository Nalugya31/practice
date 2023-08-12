from django.shortcuts import render, redirect
from .forms import BiodataForm
from .models import Biodata

def biodata(request):
    if request.method == 'POST':
        form = BiodataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BiodataForm()
    return render(request, 'biodata.html', {'form': form})

def success(request):
    return render(request, 'success.html')
