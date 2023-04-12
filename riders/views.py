from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Rider
from .forms import RiderForm

# Create your views here.

class RidersView(ListView):
    template_name = 'riders/index.html'
    model = Rider
    context_object_name = 'riders'

class CreateRiderView(CreateView):
    form_class = RiderForm
    template_name = 'riders/create-rider.html'
    model = Rider
    success_url = '/riders/'

class RidersDetailsView(DetailView):
    model = Rider
    template_name = 'riders/rider-details.html'
    context_object_name = 'rider'
 

