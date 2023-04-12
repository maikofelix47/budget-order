from django import forms
from .models import Dispatch

class DispatchForm(forms.Form):
    class Meta:
        model = Dispatch
        fields = '__all__'