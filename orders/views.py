from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Order,OrderDetails
from .forms import OrderForm, OrderDetailsForm
from dispatch.models import Dispatch
from django.db import connection
from django.http import HttpResponseBadRequest

# Create your views here.
class OrdersView(ListView):
    template_name = 'orders/index.html'
    model = Order
    context_object_name = 'orders'

def order_details(request,pk):
    order_detail = OrderDetails.objects.filter(order_id=pk)
    dispatch_details = Dispatch.objects.filter(order_id=pk)
    order_total = []
    order_cost = 0

    try:
        order_total = get_order_total(pk)
        order_cost = order_total[0]
    except:
       return HttpResponseBadRequest('There is an issue with the specified order')
    
    return render(request,'orders/order-details.html',{
        'order_details': order_detail,
        'order_total': order_cost,
        'order_id': pk,
        'dispatch_details': dispatch_details
    })

def get_order_total(orderId):
    with connection.cursor() as cursor:
        cursor.execute(""" 
            SELECT 
                SUM(od.quantity * p.price) as total_cost, 
                od.order_id as id
                FROM
                    orders_orderdetails od
                    join products_product p on (od.product_id = p.id)
                WHERE od.order_id =  %s
        group by od.order_id""",[orderId])
        row = cursor.fetchone()
    return row

class CreateOrderView(CreateView):
    form_class = OrderForm
    template_name = 'orders/create-order.html'
    model = Order
    success_url = '/orders'

class CreateOrderDetailView(CreateView):
    form_class = OrderDetailsForm
    template_name = 'orders/create-order-detail.html'
    model = OrderDetails
    success_url = '/orders'


