from django import forms

class QuantityTypeForm(forms.Form):
    name = forms.CharField(max_length=10)
    units = forms.CharField(max_length=10)


class ProductForm(forms.Form):
    name = forms.CharField(max_length=20)
    price = forms.DecimalField(max_digits=10,decimal_places=2)
    quantity_type = forms.IntegerField()
    quantity = forms.DecimalField()
    store = forms.IntegerField()