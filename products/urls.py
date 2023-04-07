from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductsView.as_view(), name='products'),
    path('<int:pk>',views.ProductDetailsView.as_view(), name='product'),
    path('quantity-types/',views.QuanityTypesView.as_view(),name='quantity-types'),
    path('quantity-types/<int:pk>',views.QuantityTypeDetailsView.as_view(),name='quantity-type')
]

