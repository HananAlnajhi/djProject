import imp
from operator import mod
from tabnanny import verbose
from unicodedata import name
from django.db import models
from datetime import datetime

# Create your models here.
class Brand(models.Model):
    """
    this is Brand table
    """
    name = models.CharField(max_length=100)
    orgin = models.CharField(max_length=100)
    imges = models.ImageField(upload_to="photos/%y/%m/%d")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    #class Meta:
        #ordering = ['name']
        #verbose_name = 'Hanan'


class Products(models.Model):
    """
    this is Products tables
    """
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    descreption = models.TextField()
    expir_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imges = models.ImageField(upload_to="photos/%y/%m/%d")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    DT = models.DateTimeField(default=datetime.now)
    active = models.BooleanField(default=True)

    

class Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50 )

