import imp
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Brand,Products 
from django.db.models import Count
from django.http import JsonResponse
import json
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from .forms1 import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout

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
        if request.method == 'POST':
            bname = request.POST.get('bname')
            borgin = request.POST.get('borgin')
            bimg = request.POST.get('bimg')
            context = Brand(name=bname,orgin=borgin,imges=bimg,active=1)
            if context.is_valid():
                context.save()
        template_name = 'makeup/addbrand.html'
        return render(request, template_name)
def addprodect(request): 
        if request.method == 'POST':
            pname = request.POST.get('pname')
            pkind = request.POST.get('pkind')
            pdesc = request.POST.get('pdesc')
            pdate = request.POST.get('pdate')
            price = request.POST.get('price')
            pimg = request.POST.get('pimg')
            pbrand = request.POST.get('pbrand')
            context = Products(name=pname,kind=pkind,descreption=pdesc,expir_date=pdate,price=price,imges=pimg,brand=pbrand,DT= datetime.now,active=1)
            if context.is_valid():
                context.save()
        template_name = 'makeup/addprodect.html'
        return render(request, template_name)
def login(request):
    if request.method == 'POST':
           username=request.POST.get('username')
           password=request.POST.get('password')
           user= authenticate(request, username=username, password=password)
           if user is not None:
               login(request , user)
               return redirect('cpanel')
           else:
                messages.info(request, 'Username Or Password not correct')
                return render(request, 'makeup/login.html') 

    context={}
    template_name = 'makeup/login.html'
    return render(request, template_name,context) 

def singin(request): 
    form= CreateUserForm()
    if request.method == 'POST':
           form= CreateUserForm(request.POST)
           if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created ^_^'+user)
                return redirect('login')
    context={'form':form}
    template_name = 'makeup/singin.html'
    return render(request, template_name,context)
def logout(request): 
    logout(request)
    return redirect('login')

        
