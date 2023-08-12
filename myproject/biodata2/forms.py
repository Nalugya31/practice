from django import forms
from .models import Biodata

class BiodataForm(forms.ModelForm):
    class Meta:
        model = Biodata
        fields = ['first_name', 'last_name', 'age', 'gender', 'email']