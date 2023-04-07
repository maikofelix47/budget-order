from django.contrib import admin

# Register your models here.
from .models import QuantityType, Product

class QuantyTypeAdmin(admin.ModelAdmin):
    list_display = ('name','units')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity_type','quantity','store')


admin.site.register(QuantityType,QuantyTypeAdmin)
admin.site.register(Product,ProductAdmin)
