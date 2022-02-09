from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand,Products
from django.db.models import Count
from django.http import JsonResponse
import json

# Create your views here.
"""
create views 
"""
def index(request):
    context ={}
    try:
        brandi = Brand.objects.all()
        context['brandi'] = brandi
    except Brand.DoesNotExist:
        context['error'] = 'Not Found'
    template_name = 'makeup/index.html'
    return render(request, template_name, context)

    
def brands(request):
    context ={}
    try:
        brandi = Brand.objects.all()
        context['brandi'] = brandi
    except Brand.DoesNotExist:
        context['error'] = 'Not Found'
    template_name = 'makeup/brands.html'
    return render(request, template_name, context)
def prodects(request):
    context ={}
    try:
        Prodi = Products.objects.all()
        context['Prodi'] = Prodi
    except Brand.DoesNotExist:
        context['error'] = 'Not Found'
    template_name = 'makeup/prodects.html'
    return render(request, template_name, context)

def cpanel(request): 
        context ={}
        try:
            Prodi = Products.objects.all()
            context['Prodi'] = Prodi
        except Brand.DoesNotExist:
            context['error'] = 'Not Found'
        template_name = 'makeup/cpanel.html'
        return render(request, template_name, context)
def addbrand(request): 
        context ={}
        try:
            Prodi = Products.objects.all()
            context['Prodi'] = Prodi
        except Brand.DoesNotExist:
            context['error'] = 'Not Found'
        template_name = 'makeup/addbrand.html'
        return render(request, template_name, context)
def addprodect(request): 
        context ={}
        try:
            Prodi = Products.objects.all()
            context['Prodi'] = Prodi
        except Brand.DoesNotExist:
            context['error'] = 'Not Found'
        template_name = 'makeup/addprodect.html'
        return render(request, template_name, context)
        
