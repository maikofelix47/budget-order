from django import forms
from .models import Order, OrderDetails

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = '__all__'