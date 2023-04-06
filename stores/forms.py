from django import forms
from .models import Store

class StoreForm(forms.Form):
    name = forms.CharField(max_length=20, label='Store Name')