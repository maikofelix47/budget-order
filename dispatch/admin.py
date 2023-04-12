from django.contrib import admin

# Register your models here.
from .models import Dispatch

class DispatchAdmin(admin.ModelAdmin):
    list_display = ('id','date_dispatched','status')

admin.site.register(Dispatch,DispatchAdmin)
