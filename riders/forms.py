from django import forms
from .models import Rider

class RiderForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = '__all__'