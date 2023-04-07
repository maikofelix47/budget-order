from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .forms import ProductForm, QuantityTypeForm
from .models import Product, QuantityType

# Create your views here.

class QuanityTypesView(ListView):
    template_name = 'products/quantity-types.html'
    model = QuantityType
    context_object_name = 'quantity_types'

class QuantityTypeDetailsView(DetailView):
    template_name = 'products/quantity-type.html'
    model = QuantityType
    context_object_name = 'quantity_type'

class ProductsView(ListView):
    template_name = 'products/products.html'
    model = Product
    context_object_name = 'products'

class ProductDetailsView(DetailView):
    template_name = 'products/product-details.html'
    model = Product
    context_object_name = 'product'
