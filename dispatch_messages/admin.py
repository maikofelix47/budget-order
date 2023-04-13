from django.contrib import admin

# Register your models here.
from .models import DispatchMessage

class DispatchMessageAdmin(admin.ModelAdmin):
    list_display = ('message','recepient','date_created')


admin.site.register(DispatchMessage,DispatchMessageAdmin)
