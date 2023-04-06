from django.urls import path
from . import views

urlpatterns = [
    path('',views.StoresView.as_view(), name='stores')
]
