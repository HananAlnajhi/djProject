import imp
from django import forms

class BrandsForm(forms.Form):
    name = forms.CharField(max_length=100)
    orgin = forms.CharField(max_length=100)
    imges = forms.ImageField(upload_to="photos/%y/%m/%d")
    active = forms.BooleanField(default=True)
