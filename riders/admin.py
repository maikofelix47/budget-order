from django.contrib import admin

# Register your models here.
from .models import Rider

class RiderAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone_no')

admin.site.register(Rider,RiderAdmin)
