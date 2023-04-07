from django.urls import path

from . import views

urlpatterns = [
    path('', views.OrdersView.as_view(), name='orders'),
    path('<int:pk>', views.order_details, name='order'),
]
