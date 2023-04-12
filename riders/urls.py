from django.urls import path
from . import views

urlpatterns = [
    path('', views.RidersView.as_view(),name='riders'),
    path('create-rider/', views.CreateRiderView.as_view(), name = 'add-rider'),
    path('<int:pk>/', views.RidersDetailsView.as_view(),name='rider-details')
]
