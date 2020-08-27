from django.contrib import admin
from .models import Category,Products,contactus

# Register your models here.

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(contactus)