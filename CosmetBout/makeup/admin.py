from xml.sax.handler import property_declaration_handler
from django.contrib import admin
from makeup.models import Brand , Products
# Register your models here.
admin.site.register(Brand)
admin.site.register(Products)
