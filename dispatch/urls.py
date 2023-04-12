from django.urls import path
from . import views

urlpatterns = [
    path('',views.DispatchView.as_view(),name='dispatch'),
    path('<int:pk>',views.DispatchDetailView.as_view(),name='dispatch-details')
]
