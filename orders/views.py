from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Order,OrderDetails

# Create your views here.
class OrdersView(ListView):
    template_name = 'orders/index.html'
    model = Order
    context_object_name = 'orders'

def order_details(request,pk):
    order_detail = OrderDetails.objects.filter(order_id=pk)
    print('order_details', order_detail)
    return render(request,'orders/order-details.html',{
        'order_details': order_detail
    })

