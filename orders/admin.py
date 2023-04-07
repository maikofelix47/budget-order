from django.contrib import admin
from .models import Order, OrderDetails

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','date_created')

class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderDetails._meta.fields]

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderDetails, OrderDetailsAdmin)

