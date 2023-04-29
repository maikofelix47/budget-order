from django.db import models

from stores.models import Store

# Create your models here.

class QuantityType(models.Model):
    name = models.CharField(max_length=10)
    units = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.name}"



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity_type = models.ForeignKey(QuantityType,on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10,decimal_places=2)
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.store.name},{self.quantity} {self.quantity_type}"
