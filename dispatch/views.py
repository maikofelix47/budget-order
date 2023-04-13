from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponseNotFound

from .models import Dispatch
from orders.models import OrderDetails
from .forms import DispatchForm

from django.db import connection

# Create your views here.

class DispatchView(ListView):
    template_name = 'dispatch/index.html'
    model = Dispatch
    context_object_name = 'dispatch'

class DispatchDetailView(DetailView):
    template_name = 'dispatch/dispatch-details.html'
    model = Dispatch
    context_object_name = 'dispatch'

def create_dispatch_order(request,orderId):
    dispatch_data = get_dispatch_detail_data(orderId)
    dispatch_details = {}
    try:
        dispatch_details['rider'] = dispatch_data[2]
        dispatch_details['message'] = dispatch_data[3]
        dispatch_details['rider_name'] = dispatch_data[4]
        dispatch_details['total_cost'] = dispatch_data[5]
    except:
        return HttpResponseNotFound('Dispatch detailsnot found')

    return render(request,'dispatch/dispatch-order.html',{
        "dispatch_details": dispatch_details
    })

def get_dispatch_detail_data(orderId):
    with connection.cursor() as cursor:
        cursor.execute(""" 
            SELECT 
            od.order_id as id,
            od.order_id,
            od.rider_id,
            GROUP_CONCAT(CONCAT(p.name,
                        '-',
                        p.quantity,
                        qt.units,
                        '(',
                        '@',
                        p.price,
                        ' x ',
                        od.quantity,
                        ')',
                        '-',
                        s.name)
                SEPARATOR '\n') AS message,
            CONCAT(r.first_name,' ',r.last_name) AS rider_name,
            SUM(od.quantity * p.price) AS total_cost
        FROM
            budget_order.orders_orderdetails od
                JOIN
            products_product p ON (p.id = od.product_id)
                JOIN
            riders_rider r ON (od.rider_id = r.id)
                JOIN
            stores_store s ON (s.id = p.store_id)
                JOIN
            products_quantitytype qt ON (qt.id = p.quantity_type_id)
        WHERE
            od.order_id = %s
        GROUP BY od.order_id , od.rider_id;
            """,[orderId])
        row = cursor.fetchone()
    return row

def dispatch_order(request):
    pass

