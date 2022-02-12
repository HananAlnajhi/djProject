from dataclasses import field
import imp
from pyexpat import model
from unittest import mock
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class BrandsForm(forms.Form):
    name = forms.CharField(max_length=100)
    orgin = forms.CharField(max_length=100)
    imges = forms.ImageField(upload_to="photos/%y/%m/%d")
    active = forms.BooleanField(default=True)
    
class ProdectForm(forms.Form):
    name = forms.CharField(max_length=100)
    kind = forms.CharField(max_length=100)
    descreption = forms.TextField()
    expir_date = forms.DateField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    imges = forms.ImageField(upload_to="photos/%y/%m/%d")
    brand = forms.ForeignKey(max_length=100)
    DT = forms.DateTimeField(default=datetime.now)
    active = forms.BooleanField(default=True)
class CreateUserForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['username','email','password1','password2']
    
