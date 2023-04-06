from django.shortcuts import render
from django.views.generic import ListView
from .models import Store

# Create your views here.

class StoresView(ListView):
    template_name = 'stores/index.html'
    model = Store
    context_object_name = 'stores'

