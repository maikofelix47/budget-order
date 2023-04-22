from django.shortcuts import render
from django.views.generic import ListView,View
from django.views.generic.edit import CreateView
from .models import Order,OrderDetails
from .forms import OrderForm, OrderDetailsForm
from dispatch.models import Dispatch
from django.db import connection
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from products.models import Product
from riders.models import Rider

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
        if order_total is not None:
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

class CreateOrderDetailView(View):
    form_class = OrderDetailsForm
    model = OrderDetails
    template_name = 'orders/create-order-detail.html'
    def get(self,request,orderId):
        initial = {"order": orderId}
        form = OrderDetailsForm(initial=initial)
        return render(request,self.template_name,{
            'form': form,
            'order_id': orderId
        })
    def post(self,request,orderId):
        form = self.form_class(request.POST)
        if form.is_valid():
            form_details = request.POST
            order = order = Order.objects.get(pk=orderId)
            product = Product.objects.get(pk=int(form_details['product']))
            rider = Rider.objects.get(pk=int(form_details['rider']))
            order_details = OrderDetails(order=order,product=product,rider=rider,quantity=form_details['quantity'])
            order_details.save()
            return HttpResponseRedirect('/orders')
        return render(request,self.template_name,{
            'form': form,
            'order_id': orderId
        })


