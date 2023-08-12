from django import forms

class BiodataForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    email = forms.EmailField()