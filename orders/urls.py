from django.urls import path

from . import views

urlpatterns = [
    path('', views.OrdersView.as_view(), name='orders'),
    path('<int:pk>', views.order_details, name='order'),
    path('create-order/', views.CreateOrderView.as_view(),name='create-order'),
    path('create-order-item/<int:orderId>', views.CreateOrderDetailView.as_view(),name='create-order-detail')
]
