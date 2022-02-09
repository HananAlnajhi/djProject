from django.urls import path
from django.http import HttpResponse
from . import views

"""
create urls for makeup app
"""
urlpatterns = [
    path('',views.index, name='index'),
    path('brands/',views.brands, name='brands'),
    path('prodects/',views.prodects, name='prodects'),
    path('cpanel/',views.cpanel, name='cpanel'),
    path('addbrand/',views.addbrand, name='addbrand'),
    path('addprodect/',views.addprodect, name='addprodect'),
]
