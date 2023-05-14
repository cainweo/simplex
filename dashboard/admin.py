from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group


admin.site.site_header = 'Simplex Staff '


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',  'category','quantity')
    list_filter = ['category']


# Register your models here.
admin.site.register(Product, ProductAdmin) # mettre product dans admin panel# 
admin.site.register(Order) # mettre order dans admin panel# 
