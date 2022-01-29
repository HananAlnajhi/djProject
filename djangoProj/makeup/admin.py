from django.contrib import admin

# Register your models here.
from makeup.models import Brand , Products
admin.site.register(Brand)
admin.site.register(Products)