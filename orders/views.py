from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Sum
from .models import Order,OrderDetails

# Create your views here.
class OrdersView(ListView):
    template_name = 'orders/index.html'
    model = Order
    context_object_name = 'orders'

def order_details(request,pk):
    order_detail = OrderDetails.objects.filter(order_id=pk)
    order_total = order_detail.raw("""SELECT 
            SUM(od.quantity * p.price) as total_cost, 
            od.order_id as id
            FROM
                orders_orderdetails od
                join products_product p on (od.product_id = p.id)
            WHERE od.order_id =  %s
    group by od.order_id;
    """,[pk])
    return render(request,'orders/order-details.html',{
        'order_details': order_detail,
        'order_total': order_total[0]
    })

