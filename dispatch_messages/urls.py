from django.urls import path
from . import views

urlpatterns = [
    path('', views.DispatchMessagesView.as_view(),name='dispatch-messages'),
]