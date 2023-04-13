from django.urls import path
from . import views

urlpatterns = [
    path('',views.DispatchView.as_view(),name='dispatch'),
    path('<int:pk>',views.DispatchDetailView.as_view(),name='dispatch-details'),
    path('create-dispatch-order/<int:orderId>', views.dispatch_order,name='create-dispatch-order'),
    path('dispatch-order/', views.dispatch_order,name='create-dispatch-order')
]
