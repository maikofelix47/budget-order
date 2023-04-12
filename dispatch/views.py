from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Dispatch
from .forms import DispatchForm

# Create your views here.

class DispatchView(ListView):
    template_name = 'dispatch/index.html'
    model = Dispatch
    context_object_name = 'dispatch'

class DispatchDetailView(DetailView):
    template_name = 'dispatch/dispatch-details.html'
    model = Dispatch
    context_object_name = 'dispatch'
