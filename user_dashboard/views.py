from django.shortcuts import render

from orders.models import Order,OrderDetails
from products.models import Product, QuantityType
from stores.models import Store
from riders.models import Rider


# Create your views here.

def user_dashboard(request):
    total_orders = Order.objects.count()
    total_products = Product.objects.count()
    total_stores = Store.objects.count()
    total_qt = QuantityType.objects.count()
    total_riders = Rider.objects.count()
    monthly_expenditure = get_last_six_months_monthly_expenditure()
    return render(request,'user_dashboard/index.html',{
         'total_orders': total_orders,
         'total_products': total_products,
         'total_stores': total_stores,
         'total_qt': total_qt,
         'total_riders': total_riders,
         'monthly_expenditure': monthly_expenditure
    })

def get_last_six_months_monthly_expenditure():
    monthly_expenditure = OrderDetails.objects.raw("""SELECT 
        1 as id,
        SUM(od.quantity * p.price) AS total_expenditure,
        DATE_FORMAT(od.date_created, '%%Y-%%m') AS month
        FROM
            orders_orderdetails od
                JOIN
            products_product p ON (od.product_id = p.id)
        WHERE
            DATE(od.date_created) >= (LAST_DAY(CURDATE()) - INTERVAL 6 MONTH)
                AND DATE(od.date_created) <= LAST_DAY(CURDATE())
        GROUP BY DATE_FORMAT(od.date_created, '%%Y-%%m');""")

    return monthly_expenditure

