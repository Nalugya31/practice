# practice this for the form that doesnt post
First, make sure you have Python and Django installed on your computer. You can check if you have Python installed by typing python --version in your terminal. If you don't have it installed, you can download it from the official website (https://www.python.org/downloads/). To check if you have Django installed, type django-admin --version in your terminal. If you don't have it installed, you can install it using pip by typing pip install Django.

Once you have Django installed, open your terminal and navigate to the directory where you want to create your project.

Type django-admin startproject myproject in your terminal to create a new Django project called "myproject".

Navigate to the newly created project directory by typing cd myproject.

Now we need to create a new app within our project. Type python manage.py startapp biodata in your terminal to create a new app called "biodata".

Open the biodata/views.py file and add the following code:
from django.shortcuts import render
from .forms import BiodataForm

def biodata(request):
    form = BiodataForm()
    return render(request, 'biodata.html', {'form': form})
views.py file:
from django.shortcuts import render
from .forms import BiodataForm

def biodata(request):
    form = BiodataForm()
    return render(request, 'biodata.html', {'form': form})
forms.py file
from django import forms

class BiodataForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    email = forms.EmailField()
    html:
    <!DOCTYPE html>
<html>
<head>
    <title>Biodata Form</title>
</head>
<body>
    <h1>Biodata Form</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>
urls.py
from django.urls import path
from biodata.views import biodata

urlpatterns = [
    path('biodata/', biodata, name='biodata'),
]

    

    
    

